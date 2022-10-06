from django.forms import ModelForm
from . models import Bus,Route

class BusForm(ModelForm):
    class Meta:
        model = Bus
        fields = ['bus_plate_number','bus_number','bus_type','bus_detail','number_of_seats']

""" class Route(models.Model):
    bus_brand = models.ForiegnKey(BusBrand, related_name="route_admin")
#  the two cities should be foreign  key for city
    first_city = models.CharField(max_length=255, null=True)
    second_city = models.CharField(max_length=255, null=True)
    # name=models.CharField(max_length=255, null=True)
    via_cities = models.CharField(max_length=255, null=True)
    travel_distance=models.IntegerField(null=True)
    travel_aproximate_time=models.CharField(max_length=255, null=True)
    single_seat_price=models.IntegerField(null=True)
    travel_facilities=models.CharField(max_length=255, null=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)"""
    
class RouteForm(ModelForm):
    class Meta:
        model = Route
        fields = ['first_city','second_city','via_cities','travel_distance','travel_aproximate_time','single_seat_price','travel_facilities']