from django.urls import path
from .views.userViews  import Record, Login, Logout, UserView

urlpatterns = [
    path('users/register/', Record.as_view(), name="register"),
    path('users/login/', Login.as_view(), name="login"),
    path('users/logout/', Logout.as_view(), name="logout"),
    path('users/', UserView.as_view(), name='user-list'),
    path('users/<int:id>', UserView.as_view(), name='user-info'),
]