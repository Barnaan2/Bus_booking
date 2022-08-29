from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="system_admin_index"),
    path('manage_bus_brand/',views.manage_bus_brand,name='manage_bus_brand'),
    # path('add_bus_brand/',views.add_bus_brand,name="add_bus_brand"),
    path('edit_bus_brand/<str:id>/',views.update_bus_brand,name="update_bus_brand")
 ]
