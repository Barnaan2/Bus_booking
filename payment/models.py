from django.db import models
from django.contrib.auth.models import User
from django_softdelete.models import SoftDeleteModel
from booker.models import SubRoute
# from booking.models import BookingRequest

# Create your models here.

class PaymentMethod(SoftDeleteModel, models.Model):
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



class PaymentInformation(SoftDeleteModel,models.Model):
    subroute = models.ForeignKey(SubRoute , on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    account_holder = models.CharField(max_length=100)
    account_number = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    verified = models.BooleanField(default=False, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
            ordering = ('-created', '-updated')

    def __str__(self):
        return self.account_number


    
# class Paid(SoftDeleteModel, models.Model):
#     payment_information = models.ForeignKey(PaymentInformation, on_delete=models.CASCADE)
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