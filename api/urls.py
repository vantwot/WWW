from django.urls import path
from .views.userViews import UserAuthorizedView, RegisterView, LoginView, LogoutView, UserView

urlpatterns = [
    path('users/register/', RegisterView.as_view(), name = 'register'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/logout/', LogoutView.as_view(), name='logout'),
    path('users/user-authenticated/', UserAuthorizedView.as_view(), name='users_authenticated'),
    path('users/', UserView.as_view(), name='users_list'),
    path('users/<int:id>', UserView.as_view(), name='user_info'),
]