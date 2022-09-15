from django.urls import path
from . import views

urlpatterns= [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('', views.home, name="home"),
    path('sub-route/<str:pk>/', views.subRoute, name="sub-route"),
    path('my-booking/<str:pk>/', views.myBooking, name="my-booking"),
    # path('pay/<str:pk>/booking', views.pay, name="pay"),
    
]