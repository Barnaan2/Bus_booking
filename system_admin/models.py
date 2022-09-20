from django.db import models
from account.models import User

# Create your models here.

class BusBrand(models.Model):
    user=models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    number_of_buses = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created', '-updated')

    def __str__(self):
        return self.name
    
class City(models.Model):
    name = models.CharField(max_length=55, unique=True)
    region = models.CharField(max_length=55, null=True)
    country = models.CharField(max_length=55, null=True, default='Ethiopia')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

# class BusAdmin(models.Model):
#     user=models.ForeignKey(User, null=True, on_delete=models.CASCADE)
#     bus_brand=models.ForeignKey(BusBrand, null=True, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.bus_brand.name


    



