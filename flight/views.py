from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import Customer, Flight, Booking, City, Company, Airport
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import django.contrib.auth
from .modify import *
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
    cities = City.objects.all()
    name = request.session.get('name')

    return render(request, "flight/index.html", locals())

def update(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('flight:update'))
    user = request.user;
    customer = Customer.objects.get(user=user)
    name = customer.name
    id_number = customer.id_number
    phone_number = customer.phone_number
    return render(request, "flight/update.html", locals())

def check(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('flight:login'))
    user = request.user;
    customer = Customer.objects.get(user=user)
    name = customer.name
    bookings = Booking.objects.filter(customer=customer)
    available_flights=[]
    for booking in bookings:
        flight = booking.flight
        flight.arrive_time1 = addzero(str(flight.arrive_time.hour)) + ":" + addzero(str(flight.arrive_time.minute))
        flight.leave_time1 = addzero(str(flight.leave_time.hour)) + ":" + addzero(str(flight.leave_time.minute))
        flight.ticket_price1 = int(booking.booking_price)
        available_flights.append(flight)
    return render(request, "flight/check.html", locals())


def result(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('flight:login'))
    cities = City.objects.all()
    companies = Company.objects.all()
    user = request.user;
    customer = Customer.objects.get(user=user)
    name = customer.name
    arrive_city1 = int(request.POST.get('arrive-city'))
    leave_city1 = int(request.POST.get('leave-city'))
    leave_date1 = request.POST.get('leave-date')
    start_price = request.POST.get('start-price')
    end_price = request.POST.get('end-price')
    company1 = request.POST.get('company')
    company1 = '0' if company1 is None else company1
    company1 = int(company1)
    arrive_city = City.objects.get(pk=arrive_city1)
    leave_city = City.objects.get(pk=leave_city1)
    leave_date = datetime.strptime(leave_date1, "%Y 年 %m 月 %d 日")
    if company1 == 0:
        flights = Flight.objects.filter(leave_city=leave_city, arrive_city=arrive_city)
    else:
        flights = Flight.objects.filter(leave_city=leave_city, arrive_city=arrive_city, flight_company=Company.objects.get(pk=company1))
    available_flights = []
    for flight in flights:
        if flight.leave_time.date() == leave_date.date():
            if start_price is not None and start_price.strip() != "" and flight.ticket_price < float(start_price):
                continue
            if end_price is not None and end_price.strip() != "" and flight.ticket_price > float(end_price):
                continue
            flight.arrive_time1 = addzero(str(flight.arrive_time.hour)) + ":" + addzero(str(flight.arrive_time.minute))
            flight.ticket_price1 = int(flight.ticket_price)
            flight.ticket_per = int(flight.ticket_bought * 100 / flight.ticket_number)
            available_flights.append(flight)
    start_price = '' if start_price is None else start_price
    end_price = '' if end_price is None else end_price        
    sort_way = request.POST.get("sort-way")
    sort_sequence = request.POST.get("sort-sequence")
    rev = True if sort_sequence == '2' else False
    if sort_way == '1':
        available_flights.sort(key=lambda x:x.leave_time, reverse=rev)
    elif sort_way == '2':
        available_flights.sort(key=lambda x:x.arrive_time, reverse=rev)
    elif sort_way == '3':
        available_flights.sort(key=lambda x:x.ticket_price1, reverse=rev)
    elif sort_way == '4':
        available_flights.sort(key=lambda x:x.ticket_per, reverse=rev)
    elif sort_way == '5':
        available_flights.sort(key=lambda x:x.arrive_time-x.leave_time, reverse=rev)
    
    return render(request, "flight/result.html", locals())


def login_solve(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)
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
    phone_number = request.POST.get("phone_number")
    try:
        user = User.objects.create_user(username=username, password=password)
    except Exception as e:
        return HttpResponse(2)
    user.save()
    customer = Customer(user=user, name=name, id_number=id_number, phone_number=phone_number)
    customer.save()
    return HttpResponse(1)

def update_solve(request):
    user = request.user;
    customer = Customer.objects.get(user=user)
    name = customer.name
    id_number = request.POST.get("id_number")
    phone_number = request.POST.get("phone_number")
    customer.id_number = id_number
    customer.phone_number = phone_number
    customer.name = name
    customer.save()
    return HttpResponse(1)

def result_booking(request):
    flight_id = request.POST.get("flight_id")
    user = request.user;
    customer = Customer.objects.get(user=user)
    name = customer.name
    flight = Flight.objects.get(flight_id=flight_id)
    booking = Booking(flight=flight,customer=customer,booking_price=flight.ticket_price)
    if (flight.ticket_bought >= flight.ticket_number):
        return HttpResponse("2")    
    flight.ticket_bought += 1
    flight.save()
    booking.save()
    return HttpResponse("1")

def check_booking(request):
    flight_id = request.POST.get("flight_id")
    user = request.user;
    customer = Customer.objects.get(user=user)
    name = customer.name
    flight = Flight.objects.get(flight_id=flight_id)
    booking = Booking.objects.filter(flight=flight,customer=customer,booking_price=flight.ticket_price)[0]
    flight.ticket_bought -= 1
    flight.save()
    booking.delete()
    return HttpResponse("ok")

def logout(request):
    django.contrib.auth.logout(request)
    print(1)
    return HttpResponse("ok")
