import json
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.views import View
from api.models.userModels import User

# Create your views here.

class UserView(View):
  
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
