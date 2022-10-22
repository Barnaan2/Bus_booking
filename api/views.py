from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from booker.models import SubRoute
from system_admin.models import BusBrand
from . serial import BusBrandSerail, SubRouteSerial


@api_view(['GET'])
def index(request):
    endpoints = {
    'BusBrand': 'https//:afroperiabus.com/busbrnad//',
     'user': 'https//:afroperiabus.com/busbrnad//',
    'booking ': 'https//:afroperiabus.com/busbrnad//',
    'route': 'https//:afroperiabus.com/busbrnad//',
    'payment': 'https//:afroperiabus.com/busbrnad//',
    }
    return Response(endpoints)

@api_view(['GET'])
def bus_brand(request):
   bus_brand = BusBrand.objects.all()
   serialized_bus_brand = BusBrandSerail(bus_brand,many=True)
   return Response(serialized_bus_brand.data)

@api_view(['GET'])
def route(request):
   routes= {
    'is this for routes?': 'yes its. now this si just place holder '
   }
   
   return Response(routes)

@api_view(['GET'])
def sub_route(request):
   subroute = SubRoute.objects.all()
   dat = SubRouteSerial(subroute,many=True)
   return Response(dat.data)

