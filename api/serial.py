from statistics import mode
from rest_framework import serializers
from system_admin.models import BusBrand

class BusBrandSerail(serializers.ModelSerializer):
    class Meta:
        model = BusBrand
        fields = '__all__'