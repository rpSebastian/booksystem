from django.contrib import admin
from flight.models import *
# Register your models here.

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_company', 'flight_id','leave_city', 'leave_airport', 'leave_time', 'arrive_city', 'arrive_airport', 'arrive_time','ticket_price')
   
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'name','id_number')

@admin.register(Booking)
class Booking(admin.ModelAdmin):
    list_display = ('customer', 'flight', 'booking_price')

admin.site.register(Company)
admin.site.register(City)
admin.site.register(Airport)

