from django.contrib import admin
from . models import PaymentInformation, PaymentMethod,FinishPayment
 # Register your models here.
admin.site.register(PaymentInformation)
admin.site.register(PaymentMethod)
admin.site.register(FinishPayment)