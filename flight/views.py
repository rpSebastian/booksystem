from django.shortcuts import render;
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Customer, Flight, Booking

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
    
def login(request):
    return render(request, "flight/login.html", locals())    

def register(request):
    return render(request, "flight/register.html", locals())    



def login_solve(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    # print(request.POST)
    # print(username)
    # print(password)
    # user = authenticate(username = username,password = password)
    # if user is not None and user.is_active:
    #     auth.login(request,user)
    #     team_user = Team_User.objects.get(user = user)
    #     team_name = team_user.teamname
    #     request.session['teamname'] = team_name
    #     print("right")
    #     print(request.session['teamname'])
    #     return HttpResponse(1)
    # else:
    #     return HttpResponse(2)
    return HttpResponse("ok")

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