from django.forms import ModelForm
from . models import BusBrand

class BusBrandForm(ModelForm):
    class Meta:
        model = BusBrand
        field = ['name','head_quarter','number_of_buses']

