from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='system_admin'),
   
    # manage payment methods
    path('manage_payment_method/', views.payment_method, name='manage_payment_method'),
    path('manage_payment_method/add_payment_method', views.add_payment_method, name='add_payment_method'),
    path('manage_payment_method/update_payment_method/<str:id>/', views.update_payment_method, name='update_payment_method'),
   #CUSTOEMR PAYMENT
    path('pay/<str:id>/', views.pay, name='pay'),
    path('pay/payment_detail/<str:br_id>/<str:pi_id>/', views.payment_detail, name='payment_detail'),
    #HOTEL MANAGE ONE'S PAYMENT INFORMATIONS
 path('add_payment_information/', views.add_payment_information, name='add_payment_information'),


]
