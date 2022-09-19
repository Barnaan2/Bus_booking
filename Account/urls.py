from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('register/', views.register, name='register'),
    # path('edit/', views.update_profile, name='edit'),
    path('booker_profile/', views.booker_profile, name='booker_profile'),
     path('system_admin_profile/', views.system_admin_profile, name='system_admin_profile'),
      path('bus_admin_profile/', views.bus_admin_profile, name='bus_admin_profile'),
     path('customer_profile/', views.profile, name='profile'),
    path('logout/', views.logout_page, name='logout'),


]
