from django.contrib import admin
from .models import PaymentInformantion, PaymentMethod
# Register your models here.

admin.site.register(PaymentInformantion)
admin.site.register(PaymentMethod)