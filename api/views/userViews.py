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

from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from ..models.userModels import User
from ..serializers.userSerializers import UserSerializer, UserLoginSerializer, UserLogoutSerializer


class Record(generics.ListCreateAPIView):
    # get method handler
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Login(generics.GenericAPIView):
    # get method handler
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = UserLoginSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)


class Logout(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserLogoutSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = UserLogoutSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)

class UserView(APIView):
  @method_decorator(csrf_exempt)

  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)
    
  def get(self, req, id=0):
    if id>0:
        users = list(User.objects.filter(id=id).values('id', 'username', 'first_name', 'last_name', 'email', 'adress', 'identification', 'token', 'password', 'role'))
        if len(users)>0:
          user = users[0]
          datos = {'message': 'Success', 'users': user}
        else:
          datos = {'message': 'Error', "users": []}
        return JsonResponse(datos)
    else: 
      users = list(User.objects.values('id', 'username', 'first_name', 'last_name', 'email', 'adress', 'identification', 'token'))
      if len(users)>0:
        datos = {'message': 'Success', 'users': users}
      else:
        datos = {'message': 'Error', "users": []}
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
      user.username=jd['username']
      user.first_name=jd['first_name']
      user.adress=jd['adress']
      user.email=jd['email']
      user.identification=jd['identification']
      user.password=jd['password']
      user.role=jd['role']
      user.last_name=jd['last_name']
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
