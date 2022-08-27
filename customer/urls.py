from django.urls import path
from . import views

urlpatterns= [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('', views.home, name="home"),
    path('route/<str:pk>/', views.route, name="route"),
    path('booking/<str:pk>/', views.booking, name="booking"),
    path('my-booking/<str:pk>/', views.myBooking, name="my-booking"),
    
]