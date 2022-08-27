from django.db import models
from django.contrib.auth.models import User




class Bus(models.Model):
    name=models.CharField(max_length=255, null=True)
    bus_admin=models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_buses=models.IntegerField()
    about=models.CharField(max_length=255, null=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
