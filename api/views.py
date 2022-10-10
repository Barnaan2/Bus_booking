from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from system_admin.models import BusBrand
from . serial import BusBrandSerail


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
   sub_routes= {
    'is this for sub-rotues?': 'yes its. now this si just place holder '
   }
   
   return Response(sub_routes)

