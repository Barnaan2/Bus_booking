from django.db import models
from account.models import User
from system_admin.models import  BusBrand, City

# Create your models here.

class Bus(models.Model):
    bus_brand = models.ForeignKey(BusBrand, on_delete=models.CASCADE, null=True)
    bus_plate_number = models.IntegerField()
    bus_number=models.CharField(max_length=200, null=True)
    bus_type=models.CharField(max_length=200, null=True)
    bus_detail=models.CharField(max_length=200, null=True)
    number_of_seats=models.IntegerField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str((self.bus_brand.name, self.bus_number,self.bus_plate_number))

class Route(models.Model): 
#  the two cities should be foreign  key for city
    bus_brand = models.ForeignKey(BusBrand, on_delete=models.CASCADE, null=True)
    first_city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    second_city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, related_name="second_city")
    via_cities = models.CharField(max_length=255, null=True)
    travel_distance=models.IntegerField(null=True)
    travel_aproximate_time=models.CharField(max_length=255, null=True)
    single_seat_price=models.IntegerField(null=True)
    travel_facilities=models.CharField(max_length=255, null=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str((self.first_city,self.second_city))
     
   
"Because every Route may have more than one bus"


class SubRouteAdmin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    admin_at_city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    route = models.ForeignKey(Route, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return ((self.user.username))
        

# class SubRouteBusAdmin(models.Model):
#     user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     subroute_bus=models.ManyToManyField(Single_Bus)
    
#     def __str__(self):
#         return (self.user.username)

"""I added this class for seat"""
"You need to add a bunch of seat_no (1, 2,3,4,5,6,..."
"Then we will do on how to display seat lists based on a particular bus number of seat"
"Before you go to book please first add seat"
# class Seat(models.Model):
#     seat_no=models.IntegerField()
    
#     def __str__(self):
#         return str(self.seat_no) 
    
