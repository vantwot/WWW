from django.urls import path
from .views.userViews  import Record, Login, Logout, UserView
from django.urls import path, include
from .views.userViews import UserView
from api.views.eventosViews import EventoViewSet

urlpatterns = [
    path('eventos/', EventoViewSet.as_view(), name='eventos_list'),
    path('users/register/', Record.as_view(), name="register"),
    path('users/login/', Login.as_view(), name="login"),
    path('users/logout/', Logout.as_view(), name="logout"),
    path('users/', UserView.as_view(), name='user-list'),
    path('users/<int:id>', UserView.as_view(), name='user-info'),
]