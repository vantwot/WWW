from django.contrib import admin
from .models.userModels import User
from .models.eventos import Eventos

# Register your models here.
admin.site.register(User)
admin.site.register(Eventos)