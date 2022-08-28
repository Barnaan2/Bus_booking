from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="system_admin_index"),
    path('manage_bus_brand/',views.getBus,name='manage_bus_brand'),
    path('edit_bus_brand/<str:id>/',views.update_bus,name="edit_bus_brand")
 ]
