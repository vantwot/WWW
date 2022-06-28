import json
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.views import View
from api.models.userModels import User
from api.serializers.userSerializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import datetime, jwt

# Create your views here.
class RegisterView(APIView):
  def post(self, request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

class LoginView(APIView):
  def post(self, request):
    email = request.data['email']
    password = request.data['password']

    user = User.objects.filter(email=email).first()

    if user is None:
      raise AuthenticationFailed('User not found')

    if not user.check_password(password):
      raise AuthenticationFailed('Incorrect Password')

    payload = {
      "id": user.id,
      "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
      "iat": datetime.datetime.utcnow()
    }

    token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

    response =  Response()

    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
      'jwt': token
    }

    return response

class UserAuthorizedView(APIView):
  
  """@method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)"""

  def get(self, request):
    token = request.COOKIES.get('jwt')

    if not token:
      raise AuthenticationFailed('Unauthorized')

    try:
      payload = jwt.decode(token, 'secret', algorithm=['HS256'])
    except jwt.ExpiredSignatureError:
      raise AuthenticationFailed('Unauthorized')

    user = User.objects.filter(id=payload['id']).first()
    serializer = UserSerializer(user)

    return Response(serializer.data)

class LogoutView(APIView):
  def post(self, request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
      'message': 'success'
    }
    return response

class UserView(APIView):
  @method_decorator(csrf_exempt)

  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)
    
  def get(self, req, id=0):
    if id>0:
        users = list(User.objects.filter(id=id).values())
        if len(users)>0:
          user = users[0]
          datos = {'message': 'Success', 'users': user}
        else:
          datos = {'message': 'Error'}
        return JsonResponse(datos)
    else: 
      users = list(User.objects.values())
      if len(users)>0:
        datos = {'message': 'Success', 'users': users}
      else:
        datos = {'message': 'Error'}
      return JsonResponse(datos)

  def post(self, req):
    jd = json.loads(req.body) #Organiza los datos del req en formato json
    User.objects.create(name = jd['name'], lastname = jd['lastname'], adress = jd['adress'])
    datos = {'message': 'Success'}
    return JsonResponse(datos)

  def put(self, req, id):
    jd = json.loads(req.body)
    users = list(User.objects.filter(id=id).values())
    if len(users)>0:
      user = User.objects.get(id=id)
      user.name=jd['name']
      user.lastname=jd['lastname']
      user.adress=jd['adress']
      user.save()
      datos = {'message': 'Success'}
    else:
      datos = {'message': 'Error'}
    return JsonResponse(datos)

  def delete(self, req, id):
    users = list(User.objects.filter(id=id).values())
    if len(users)>0:
      User.objects.filter(id=id).delete()
      datos = {'message': 'Success'}
    else:
      datos = {'message': 'Error'}
    return JsonResponse(datos)
