from django.urls import path
from . import views

urlpatterns= [
    path('home/', views.home, name="subroute_home"),
    path('manage_subroute/',views.manage_subroute, name="manage_subroute"),
   path('add_subroute/',views.add_subroute, name="add_subroute"),
   path('update_subroute/',views.update_subroute, name="update_subroute"),
    # path('booking-request/<str:pk>/', views.bookingRequest, name="booking-request"),
    # path('paid-unpaid/<str:pk>/', views.finishPaymentStatus, name="paid-unpaid"),
]