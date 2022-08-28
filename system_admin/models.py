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

class BusAdmin(models.Model):
    user=models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    bus=models.ForeignKey(Bus, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.bus.name

# Create your models here.

class BusBrand(models.Model):
    name = models.CharField(max_length=50)
    head = models.CharField(max_length = 50)
    number_buses = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created', '-updated')

    def __str__(self):
        return self.name
    



