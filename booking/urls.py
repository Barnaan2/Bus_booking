from django.urls import path
from . import views

urlpatterns= [
    path('<str:pk>/', views.booking, name="booking"),
    path('manage_booking/<str:pk>/', views.manage_booking, name="manage_booking"),
    path('passenger/<str:pk>/',views.passengers,name="passenger")

       
]