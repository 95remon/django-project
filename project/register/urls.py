from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.registerPage, name="register"), 
    path('login/', views.loginPage, name="login"), 
    
]
