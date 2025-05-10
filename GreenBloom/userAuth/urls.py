from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="user_home"),
    path('login/', views.user_login, name="login"),
    path('register/', views.user_register, name="register"),
    path('logout/', views.user_logout, name="user_logout")
    
]