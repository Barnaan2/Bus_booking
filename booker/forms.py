from django.forms import ModelForm
from . models import SubRoute

class SubRouteForm(ModelForm):
    class Meta:
        model = SubRoute
        fields = ['destination','bus','travel_date','travel_begin_time']

"""main_route=models.ForeignKey(Route, on_delete=models.CASCADE, null=True)
    bus=models.ForeignKey(SingleBus, on_delete=models.SET_NULL, null=True)
this start should set by the system its equal where the Booker is a subroute admin 
    start = models.CharField(max_length=255, null=True)
    destination=models.CharField(max_length=255, null=True)
    travel_date = models.DateField(null=True)
    travel_begin_time=models.TimeField(null=True)"""