from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name="api_index"),
    path('bus-brand/', views.bus_brand, name="api_index"),
#     path('manage_subroute/',views.manage_subroute, name="manage_subroute"),
#    path('add_subroute/',views.add_subroute, name="add_subroute"),
#    path('update_subroute/<str:id>/',views.update_subroute, name="update_subroute"),
    # path('booking-request/<str:pk>/', views.bookingRequest, name="booking-request"),
    # path('paid-unpaid/<str:pk>/', views.finishPaymentStatus, name="paid-unpaid"),
]
