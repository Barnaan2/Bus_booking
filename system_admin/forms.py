from django.forms import ModelForm
from . models import BusBrand

class BusBrandForm(ModelForm):
    class Meta:
        model = BusBrand
        fields = ['name','number_of_buses']

