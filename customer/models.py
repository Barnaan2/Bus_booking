from django.db import models
from account.models import User

# Create your models here.

# class Booking(models.Model):
#     user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     route=models.ForeignKey(Route, on_delete=models.SET_NULL, null=True)
#     sub_route=models.ForeignKey(SubRoute, on_delete=models.SET_NULL, null=True)
#     bus=models.CharField(max_length=255, null=True)
#     start=models.CharField(max_length=255, null=True)
#     destination=models.CharField(max_length=255, null=True)
#     travel_date=models.DateField(null=True)
#     travel_begin_time=models.TimeField(null=True)
#     travaler_name=models.CharField(max_length=255, null=True)
#     traveler_contact=models.CharField(max_length=255, null=True)
#     seat=models.CharField(max_length=25,  null=True)
#     updated=models.DateTimeField(auto_now=True)
#     created=models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.user.username


    
    