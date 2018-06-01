from django.shortcuts import render;
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Customer, Flight, Booking
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
    
    user = User.objects.create_user(username = username,password = password)
    user.name = name
    user.id_number = id_number
    user.save()
    user = authenticate(username = username,password = password)
    print(User.objects.get(username = username))
    team_user = Team_User.objects.create(user = user,teamname =teamname)
    team_user.save()
    return HttpResponse(1)