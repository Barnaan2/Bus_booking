
from rest_framework import serializers
from booker.models import SubRoute
from system_admin.models import BusBrand


class BusBrandSerail(serializers.ModelSerializer):
    class Meta:
        model = BusBrand
        fields = '__all__'


class SubRouteSerial(serializers.ModelSerializer):
    class Meta:
      model = SubRoute
      fields = '__all__'