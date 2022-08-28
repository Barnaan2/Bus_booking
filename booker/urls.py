from django.urls import path
from . import views

urlpatterns= [
    path('home/<str:pk>/', views.home, name="home"),
    path('booking-request/<str:pk>/', views.bookingRequest, name="booking-request"),
    path('paid-unpaid/<str:pk>/', views.finishPaymentStatus, name="paid-unpaid"),
]