from django.urls import path

from . import views

app_name = 'flight'

urlpatterns = [
    path('login', views.login, name='login'),
    
    path('login_solve', views.login_solve),
    
    path('register', views.register, name='register'),
    
    path('register_solve', views.register_solve, name='register'),
]