from urllib import request
from django.shortcuts import render


# Create your views here.

def index(request):
    return render (request,'system_admi/index.html')
