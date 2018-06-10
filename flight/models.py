from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    phone_number = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Airport(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Flight(models.Model):
    flight_id = models.CharField(max_length=10)
    flight_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    leave_city = models.ForeignKey(City, on_delete=models.CASCADE,related_name='leave_city')
    leave_airport = models.ForeignKey(Airport, on_delete=models.CASCADE,related_name='leave_airport')
    leave_time = models.DateTimeField()
    arrive_city = models.ForeignKey(City, on_delete=models.CASCADE,related_name='arrive_city')
    arrive_airport = models.ForeignKey(Airport, on_delete=models.CASCADE,related_name='arrive_airport')
    arrive_time = models.DateTimeField()
    ticket_price = models.FloatField(default=0)
    tieket_discount = models.FloatField(default=1)
    ticket_number = models.IntegerField(default=100)
    ticket_bought = models.IntegerField(default=0)

    def __str__(self):
        return str(self.flight_company) + self.flight_id + \
            " fly from " + str(self.leave_city) + " " + str(self.leave_airport) + " at " + str(self.leave_time) + \
            " to " + str(self.arrive_city) + " " + str(self.arrive_airport) + " at " + str(self.arrive_time)

class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    booking_price = models.FloatField(default=0)
    

# Create your models here.
