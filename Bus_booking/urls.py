
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  
    path('admin/', admin.site.urls),
    path('', include('customer.urls')),
    path('booker/', include('booker.urls')),
    path('system_admin/',include('system_admin.urls')),
    path('bus_admin/',include('bus_admin.urls')),
    path('account/',include('account.urls')),
    path('booking/',include('booking.urls')),
  
]

