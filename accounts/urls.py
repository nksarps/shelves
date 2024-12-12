from . import views
from django.urls import path

urlpatterns = [
    path('sign-up', views.sign_up, name='sign_up'),
    path('verify-user', views.verify_user, name='verify_user'),
    path('login', views.login, name='login'),
    path('users/<str:id>', views.get_user_by_id, name='get_user_by_id'),
    path('users', views.get_all_users, name='get_all_users'),
    path('password-reset', views.password_reset, name='password_reset'),
    path('password-reset-confirm', views.password_reset_confirm, name='password_reset_confirm'),
]