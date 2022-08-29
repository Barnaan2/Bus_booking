from django.shortcuts import render, redirect
from django.shortcuts import render
from . forms import BusBrandForm
from . models import BusBrand
from django.db.models import Q
from django.contrib import messages


# Create your views here.

def index(request):
    return render (request,'system_admin/index.html')


def manage_bus_brand(request):
    bus_brand = BusBrand.object.all()
    # this method also handles search and detail functionalities
    q = None
    if request.method == 'GET' and q != None:
        q = request.GET.get(q)
        bus_brand = BusBrand.objects.filter(
            Q(number_of_bus__icontains=q) |
            Q(name__icontains=q))
    context = {'bus_brands':bus_brand}
    return render(request,'system_admin/manage_bus_brand.html',context)
# manage the bus
# def add_bus_brand(request):
#     form = BusBrandForm()
#     if request.method == "POST":
#         form = BusBrandForm(request.POST)
#         if form.is_valid():
#                bus_brand = form.save()
               
#                return redirect('add_bus_admin', bus_brand.id)
#     context = {"form":form}
#     return render(request,'system_admin/new.html',context)

def update_bus_brand(request,id):
    bus_brand  = BusBrand.objects.get(id=id)
    form = BusBrandForm(instance = bus_brand)
    if request.method == "POST":
        form = BusBrandForm(request.POST,instance=bus_brand)
        if form.is_valid():
            form.save()
        return redirect("system_admin_index")
    context = {'form':form}
    return redirect(request,'system_admin/edit.html',context)
        
# view all buses


# # Bus admin registration
# def Bus_admin(request, id):
#     hotel = BusBrand.objects.get(id=id)
#     # user createtion form for the bus addmin
#     form = OurUserCreationForm()
#     # This role should be assigned based on the place the request come  or by some hidden input field
#     if request.method == 'POST':
#         form = OurUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()

#             BusBrand.admin.add(user)
#             messages.success(request, 'you have added new bus admin successfully')
#             return redirect('system_admin')
#         else:
#             context = {'form': form, 'hotel': hotel}
#             return render(request, 'system_admin/hotel_admin.html', context)

#     context = {'form': form, 'hotel': hotel}
#     return render(request, 'register.html', context)
   

