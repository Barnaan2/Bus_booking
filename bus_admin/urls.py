from django.urls import path
from . import views

urlpatterns= [ 
    path('home/', views.index, name="bus_admin_home"),
    path('manage_bus/',views.manage_bus, name="manage_bus"),
    path('add_bus/',views.add_bus, name="add_bus"),
    path('update_bus/<str:id>/',views.update_bus, name="update_bus"),
    # path('booking-request/<str:pk>/', views.bookingRequest, name="booking-request"),
    # path('paid-unpaid/<str:pk>/', views.finishPaymentStatus, name="paid-unpaid"),
   path('manage_route/',views.manage_route, name="manage_route"),
   path('add_route/',views.add_route, name="add_route"),
   path('update_route/<str:id>/',views.update_route, name="update_route"),
#    manage subroute admins
   path('manage_booker/',views.manage_booker, name="manage_booker"),
   path('add_booker/',views.add_booker, name="add_booker"),
   path('update_booker/<str:id>/',views.update_booker, name="update_booker"),

]