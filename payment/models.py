from django.db import models
from account.models import User
from booking.models import Booking
from bus_admin.models import SubRouteAdmin

# Create your models here.

class PaymentMethod(models.Model):
    name = models.CharField(max_length=55, unique=True)
    type = models.CharField(max_length=55)
    shortcode = models.TextField(max_length=20)
    company_logo = models.ImageField(null=True, default='payment_method.png')
    description = models.TextField(max_length=200)
    contact = models.TextField(max_length=20)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created', '-updated')

    def __str__(self):
        return self.name


""" here the paymentInformation class of each subroute is different since our model of development for this 
project is replicating the exising manual model to replace it in computerized manner . so the paymanent is made of a subroute 
that the account also must be subroute specific to manage easily."""
class PaymentInformation(models.Model):
    subroute_admin = models.ForeignKey(SubRouteAdmin, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # the payment method will be choosed from those method that the system admin added based the agrement .
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    account_holder_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    verified = models.BooleanField(default=False, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
            ordering = ('-created', '-updated')

    def __str__(self):
        return self.account_number

# when the customer is wlling to pay the customer will fillout the following form .
    
# class Paid(models.Model):
    
#     booking_request = models.ForeignKey(BookingRequest, on_delete=models.CASCADE)
#     name = models.CharField(max_length=60)
#     transaction_id = models.CharField(max_length=60)
#     expected_payment = models.FloatField()
#     amount = models.FloatField()
#     picture = models.ImageField(null=True, default='payment_method.png')
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name
# # this is needed for production but for now let just comment it out.
#     class Meta:
#         unique_together = [['booking_request', 'transaction_id']]

   
class FinishPayment(models.Model):
    booking=models.OneToOneField(Booking, on_delete=models.CASCADE, primary_key=True, related_name="finishpymnt_booking")
    # payment_method=models.ForeignKey(PaymentInformantion, on_delete=models.CASCADE, blank=True, null=True)
    payment_information = models.ForeignKey(PaymentInformation, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=60)
    # paid_by=models.CharField(max_length=255, null=True)
    transaction_id=models.CharField(max_length=255, null=True)
    picture = models.ImageField(null=True, default='payment_method.png')
    amount = models.FloatField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.full_name
    
    class Meta:
        unique_together = [['booking', 'transaction_id']]
    
    
# class FinishPaymentStatus(models.Model):
#     fnishpayment=models.OneToOneField(FinishPayment, on_delete=models.CASCADE, primary_key=True, related_name="finishpayment_status")
#     status=models.BooleanField(default=False)
    
#     def __str__(self):
#         return self.finishpayment
