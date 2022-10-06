from django.urls import path
from . import views

urlpatterns= [
    path('', views.home, name="home"),
    path('sub-route/<str:pk>/', views.subRoute, name="sub-route"),
    path('my-booking/<str:pk>/', views.myBooking, name="my-booking"),
    # path('pay/<str:pk>/booking', views.pay, name="pay"),
    
]