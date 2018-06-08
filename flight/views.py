from django.shortcuts import render;
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import Customer, Flight, Booking

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import django.contrib.auth
# Create your views here.
    
def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('flight:index'))
    return render(request, "flight/login.html", locals())    

def register(request):
    return render(request, "flight/register.html", locals())    

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('flight:login'))
    name = request.session['name']
    return render(request, "flight/index.html", locals())    
    
def login_solve(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = authenticate(username = username,password = password)
    if user is not None and user.is_active:
        django.contrib.auth.login(request, user)
        customer = Customer.objects.get(user=user)
        request.session['name'] = customer.name
        return HttpResponse(1)
    else:
        return HttpResponse(2)

def register_solve(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    name = request.POST.get("name")
    id_number = request.POST.get("id_number")
    try:
        user = User.objects.create_user(username=username, password=password)
    except Exception as e:
        return HttpResponse(2)
    user.save()
    customer = Customer(user=user, name=name, id_number=id_number)
    customer.save()
    return HttpResponse(1)

def logout(request):
    django.contrib.auth.logout(request)
    request.session['name'] = ''
    print(1)
    return HttpResponse("ok")
