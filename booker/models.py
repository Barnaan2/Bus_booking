from django.db import models
from bus_admin.models import Route
# Create your models here.
   
class PaymentMethod(models.Model):
    name = models.CharField(max_length=55)
    type = models.CharField(max_length=55)
    # logo = models.ImageField(max_length=55)
    description = models.TextField()
    shortCode = models.IntegerField()
    contact = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class PaymentInformantion(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    pyment_method = models.ManyToManyField(PaymentMethod, blank=False)
    account_holder = models.CharField(max_length=55)
    account_number = models.IntegerField()
    phone_number = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.account_holder