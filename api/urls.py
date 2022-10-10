from django.urls import path
from . import views

urlpatterns= [
    path('', views.index),
    path('bus-brand/', views.bus_brand),
    path('route/',views.route),
 path('sub_route/',views.sub_route),
#    path('update_subroute/<str:id>/',views.update_subroute, name="update_subroute"),
    # path('booking-request/<str:pk>/', views.bookingRequest, name="booking-request"),
    # path('paid-unpaid/<str:pk>/', views.finishPaymentStatus, name="paid-unpaid"),
]
