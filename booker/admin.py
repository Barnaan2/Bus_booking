from django.contrib import admin
from .models import PaymentInformantion, PaymentMethod, FinishPayment, FinishPaymentStatus
# Register your models here.

admin.site.register(PaymentInformantion)
admin.site.register(PaymentMethod)
admin.site.register(FinishPayment)
admin.site.register(FinishPaymentStatus)