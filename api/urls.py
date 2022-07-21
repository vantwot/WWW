from django.urls import path, include
from .views.userViews import UserView
from api.views.eventosViews import EventoViewSet

urlpatterns = [
    path('eventos/', EventoViewSet.as_view(), name='eventos_list'),
    path('users/', UserView.as_view(), name='users_list'),
    path('users/<int:id>', UserView.as_view(), name='user_info'),
]