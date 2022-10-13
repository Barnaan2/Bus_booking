from django.db import models
from account.models import User  
from booker.models import BusSeat
# Create your models here.

class Booking(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    bus_seat=models.ManyToManyField(BusSeat) 
    # bus=models.CharField(max_length=255, null=True)
    # start=models.CharField(max_length=255, null=True)
    # destination=models.CharField(max_length=255, null=True)
    # travel_date=models.DateField(null=True)
    # travel_begin_time=models.TimeField(null=True)
    total_price = models.FloatField(default=1000)
    # travaler_name=models.CharField(max_length=255, null=True)
    # traveler_contact=models.CharField(max_length=255, null=True)
    seat_quantity=models.IntegerField(default=1)
    status=models.CharField(max_length=25,default="Waiting")
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username

""" Keep in mind this passanger table is needed 
to generate ticket for each seats so
 it will be filled after the
payment is approved by the booker.
so finally the ticket will be sent to the bus helper (bus driver ) for validation purposes
"""
class Passanger(models.Model):
    booking = models.ForeignKey(Booking,on_delete=models.CASCADE)
    bus_seat = models.ForeignKey(BusSeat,on_delete=models.CASCADE)
    name=models.CharField(max_length=255, null=True)
    contact=models.CharField(max_length=255, null=True)

    
    