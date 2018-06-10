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
    url(r'^logout/$', views.logout),
    url(r'^result/$', views.result, name='result'),
    url(r'^result/booking/$', views.result_booking),
    url(r'^check/$', views.check, name='check'),
    url(r'^check/booking/$', views.check_booking),
    url(r'^update/$', views.update, name='update'),
    url(r'^update/solve/$', views.update_solve),
]