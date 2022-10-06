from django.urls import path
from . import views

urlpatterns= [
    path('home/', views.index, name="bus_admin_home"),
    path('manage_bus/',views.manage_bus, name="manage_bus"),
    path('add_bus/',views.add_bus, name="add_bus"),
    path('update_bus/',views.update_bus, name="update_bus"),
    # path('booking-request/<str:pk>/', views.bookingRequest, name="booking-request"),
    # path('paid-unpaid/<str:pk>/', views.finishPaymentStatus, name="paid-unpaid"),
   path('manage_route/',views.manage_route, name="manage_route"),
   path('add_route/',views.add_route, name="add_route"),
   path('update_route/',views.update_route, name="update_route"),
]