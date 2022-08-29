from django.db import models
from django.contrib.auth.models import User
from system_admin.models import Bus
# Create your models here.


class Single_Bus(models.Model):
    bus=models.ForeignKey(Bus, on_delete=models.CASCADE, null=True)
    bus_number=models.CharField(max_length=200, null=True)
    bus_type=models.CharField(max_length=200, null=True)
    bus_detail=models.CharField(max_length=200, null=True)
    number_of_seats=models.IntegerField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str((self.bus.name, self.bus_number))

class Route(models.Model):
    route_admin=models.ManyToManyField(User, related_name="route_admin")
    name=models.CharField(max_length=255, null=True)
    start=models.CharField(max_length=255, null=True)
    destination=models.CharField(max_length=255, null=True)
    via_cities=models.CharField(max_length=255, null=True)
    travel_date=models.DateField(null=True)
    travel_begin_time=models.TimeField(null=True)
    travel_distance=models.IntegerField(null=True)
    travel_aproximate_time=models.CharField(max_length=255, null=True)
    single_seat_price=models.IntegerField(null=True)
    travel_facilities=models.CharField(max_length=255, null=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.name)
     
   
"Because every Route may have more than one bus"
    
class SubRoute(models.Model):
    main_route=models.ForeignKey(Route, on_delete=models.CASCADE, null=True)
    bus=models.ForeignKey(Single_Bus, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return str((self.main_route.name, self.bus.bus.name, self.bus.bus_number)) 


class SubRouteAdmin(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    sub_route=models.ForeignKey(SubRoute, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return (self.user.username)
        

class SubRouteBusAdmin(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    subroute_bus=models.ManyToManyField(Single_Bus)
    
    def __str__(self):
        return (self.user.username)

"""I added this class for seat"""
"You need to add bunch of seat_no (1, 2,3,4,5,6,..."
"Then we will do on how to display seat lists based on a particular bus number of seat"
"Before you go to book please first add seat"
class Seat(models.Model):
    seat_no=models.IntegerField()
    
    def __str__(self):
        return str(self.seat_no) 
    
