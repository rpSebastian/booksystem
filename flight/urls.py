# from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'flight'

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^login/solve/$', views.login_solve),
    url(r'^register/$', views.register, name='register'),
    url(r'^register/solve/$', views.register_solve),
    url(r'^index/$', views.index, name='index'),
    url(r'^index/logout/$', views.logout),
]