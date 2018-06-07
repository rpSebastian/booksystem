from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=20)
    name = models.CharField(max_length=20, default="")


class Flight(models.Model):
    flight_id = models.CharField(max_length=10)
    arrive_city = models.CharField(max_length=10)
    leave_city = models.CharField(max_length=10)
    arrive_airport = models.CharField(max_length=10)
    leave_airport = models.CharField(max_length=10)
    arrive_time = models.DateTimeField()
    leave_time = models.DateTimeField()
    ticket_price = models.FloatField(default=0)
    tieket_discount = models.FloatField(default=1)
    ticket_number = models.IntegerField(default=0)

class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    booking_price = models.FloatField(default=0)


# Create your models here.
