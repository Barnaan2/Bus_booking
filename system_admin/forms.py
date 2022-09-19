from django.forms import ModelForm
from . models import BusBrand
from .models import City

class BusBrandForm(ModelForm):
    class Meta:
        model = BusBrand
        fields = ['name','number_of_buses']

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name', 'region']