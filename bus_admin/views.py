
import imp
from django.shortcuts import render, redirect
from system_admin.models import BusBrand
from . models import Bus,Route
from . forms import BusForm,RouteForm,SubrouteAdminForm
from . models import SubRouteAdmin
from account.models import User

# Create your views here.
# manage bus admim
def index(request):
    # i used this to add the right thing letter when we decide what pass to the index page.
    bus = BusBrand.objects.filter(user=request.user).first()
    context = {"bus": bus}
    return render(request,'bus_admin/home.html',context)

def manage_bus(request):
    bus_brand = BusBrand.objects.filter(user=request.user).first()
    buses = Bus.objects.filter(bus_brand=bus_brand)
    context = {"buses":buses}
    return render(request,"bus_admin/manage_bus.html",context)
 

def add_bus(request):
    form = BusForm()
    if request.method == "POST":
        form = BusForm(request.POST)
        if form.is_valid():
           bus = form.save(commit=False)
           bus.bus_brand = BusBrand.objects.filter(user=request.user).first()
           bus.save()
           return redirect('bus_admin_home')
    context = {'form':form}
    return render(request,'bus_admin/new.html',context)

def update_bus(request,id):
    bus = Bus.objects.get(id=id)
    form = BusForm(instance = bus)
    if request.method == "POST":
        form = BusForm(request.POST,instance= bus)
        if form.is_valid():
            form.save()
        return redirect("bus_admin_home")
    context = {'form':form}
    return render(request,'bus_admin/update.html',context)


def delete_bus(request,id):
      bus = Bus.objects.filter(id=id)
      if request.method == "POST":
            bus.delete()
            return redirect("bus_admin_home")
      context = {'bus': bus}
      return render(request,' ',context)


# manage route

def manage_route(request):
    bus_brand = BusBrand.objects.filter(user=request.user).first()
    routes = Route.objects.filter(bus_brand=bus_brand)
    # q=request.GET.get('q') if request.GET.get('q') != None else ''
    # routes=Route.objects.filter(id=q)
    context = {"routes":routes}
    return render(request,'bus_admin/manage_route.html',context)



def add_route(request):
    form = RouteForm()
    if request.method == "POST":
        form = RouteForm(request.POST)
        if form.is_valid():
           route =  form.save(commit=False)
           route.bus_brand = BusBrand.objects.filter(user=request.user).first()
           route.save()
           return redirect("manage_route")
    context = {'form':form}
    return render(request,'bus_admin/new.html',context)



def update_route(request,id):
    route = Route.objects.get(id=id)
    form =RouteForm(instance =route)
    if request.method == "POST":
        form =RouteForm(request.POST,instance=route)
        if form.is_valid():
            form.save()
        return redirect("manage_route")
    context = {'form':form}
    return render(request,'bus_admin/update.html',context)


def delete_route(request,id):
      route =Route.objects.get(id=id)
      if request.method == "POST":
            route.delete()
            return redirect("manage_route")
      context = {'route':route}
      return redirect(request,' ',context)


# add booker 

def manage_booker(request):
   subroute_admins = SubRouteAdmin.objects.filter(route__bus_brand = BusBrand.objects.filter(user=request.user).first())
   context = {'subroute_admins':subroute_admins} 
   return render(request,'bus_admin/manage_booker.html',context)

def add_booker(request):
    form = SubrouteAdminForm()
    if request.method == "POST":
        form = SubrouteAdminForm(request.POST)
        if form.is_valid():
            booker = form.save(commit=False)
            id = request.GET.get('id') 
            user = User.objects.get(id=id)
            booker.user = user
            booker.save()
            return redirect('manage_booker')  
    context = {'form':form}    
    return render(request,'bus_admin/new.html',context)

    
def update_booker(request,id):
    subroute_admin = SubRouteAdmin.objects.get(id=id)
    form = SubrouteAdminForm(instance=subroute_admin)
    if request.method == "POST":
        form = SubrouteAdminForm(request.POST,instance=subroute_admin)
        if form.is_valid():
            form.save()
            return redirect("manage_booker");
    context = {'form':form}
    return render(request,'bus_admin/update.html',context)


