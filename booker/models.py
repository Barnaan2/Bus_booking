from django.db import models
from bus_admin.models import Bus,SubRouteAdmin,Route
from system_admin.models import City
# from customer.models import Booking
# Create your models here.


class SubRoute(models.Model):
    subroute_admin = models.ForeignKey (SubRouteAdmin,on_delete=models.SET_NULL, null=True)
    route = models.ForeignKey(Route,on_delete=models.SET_NULL, null=True)
    bus = models.ForeignKey(Bus, on_delete=models.SET_NULL, null=True)
    """ this start should set by the system its equal where the Booker is a subroute admin at"""
    start = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    destination= models.ForeignKey(City, on_delete=models.CASCADE, null=True, related_name="destination")
    travel_date = models.DateField(null=True)
    travel_begin_time=models.TimeField(null=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str((self.start,self.destination, self.bus.bus_plate_number, self.bus.bus_number)) 


# class PaymentInformantion(models.Model):
#     route = models.ForeignKey(Route, on_delete=models.CASCADE)
#     payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE, blank=False, null=True)
#     account_holder = models.CharField(max_length=55)
#     account_number = models.IntegerField()
#     phone_number = models.IntegerField()
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return str(self.payment_method.name)
    
# class FinishPayment(models.Model):
#     booking=models.OneToOneField(Booking, on_delete=models.CASCADE, primary_key=True, related_name="finishpymnt_booking")
#     payment_method=models.ForeignKey(PaymentInformantion, on_delete=models.CASCADE, blank=True, null=True)
#     paid_by=models.CharField(max_length=255, null=True)
#     transaction_id=models.CharField(max_length=255, null=True)
#     # screenshot=
#     updated=models.DateTimeField(auto_now=True)
#     created=models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.paid_by
    
    
# class FinishPaymentStatus(models.Model):
#     fnishpayment=models.OneToOneField(FinishPayment, on_delete=models.CASCADE, primary_key=True, related_name="finishpayment_status")
#     status=models.BooleanField(default=False)
    
#     def __str__(self):
#         return self.finishpayment
    
