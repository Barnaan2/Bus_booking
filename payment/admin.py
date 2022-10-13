from django.contrib import admin
from . models import PaymentInformation, PaymentMethod
 # Register your models here.
admin.site.register(PaymentInformation)
admin.site.register(PaymentMethod)