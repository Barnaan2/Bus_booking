from django.shortcuts import render, redirect
from django.shortcuts import render
from urllib.parse import urlencode
from django.urls import reverse


from . forms import BusBrandForm,CityForm
from . models import BusBrand,City
from django.db.models import Q
from django.contrib import messages
from account.models import User
from account.forms import OurUserCreationForm
from account.views import register
from django.contrib.auth.decorators import login_required
from system_admin.decorators import only_admins



# Create your views here.

def index(request):

    return render (request,'system_admin/index.html')


# ------------------------------------------------------------------------------------------------------|
#                                                                                                      |
#   MANAGE BUSBRAND
# ------------------------------------------------------------------------------------------------------|
def manage_bus_brand(request):
    bus_brand = BusBrand.objects.all()
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
def add_bus_brand(request):
    form = BusBrandForm()
    if request.method == "POST":
        form = BusBrandForm(request.POST)
        if form.is_valid():
            bus_brand = form.save()
            base_url = reverse('register')
            user = urlencode({'id':bus_brand.id})
            url = '{}?{}'.format(base_url,user)
            return redirect(url)
    context = {"form":form}
    return render(request,'system_admin/new.html',context)

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
# def add_bus_admin(request, id):
#     bus_brand = BusBrand.objects.get(id=id)
#     # This role should be assigned based on the place the request come  or by some hidden input field 
#     user = {}
#     def get_user(request,id):
#         user = User.objects.get(id=id)
         
       
#     bus_brand.user = user
#     messages.success(request, 'you have added new bus admin successfully')
#     return redirect('system_admin_index')
        
    # context = {'form': form, 'bus_brand': bus_brand}
    # return render(request, 'system_admin/hotel_admin.html', context)
    # context = {'form': form, 'bus_brand': bus_brand}
    # return render(request, 'register.html', context)
   

   
# ------------------------------------------------------------------------------------------------------|
#                                                                                                      |
#   MANAGE CITY
# ------------------------------------------------------------------------------------------------------|
@login_required(login_url='login')
@only_admins
def city(request):
    cities = City.objects.all()
    context = {'cities': cities}
    return render(request, 'system_admin/manage_city.html', context)


@login_required(login_url='login')
@only_admins
def add_city(request):
    form = CityForm()
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('system_admin')
        else:
            messages.error(request, 'there is error in your input try again')
    context = {'form': form}
    return render(request, 'system_admin/new.html', context)


@login_required(login_url='login')
@only_admins
def update_city(request, id):
    city = City.objects.get(id=id)
    form = CityForm(instance=city)
    if request.method == "POST":
        form = CityForm(request.POST, instance=city)
        if form.is_valid():
            form.save()
            # success message
            messages.success(request, ' updated successfully')
            return redirect('system_admin')
    context = {'form': form}
    return render(request, 'system_admin/edit.html', context)


@login_required(login_url='login')
@only_admins
def delete_city(request, id):
    city = City.objects.get(id=id)
    if request.method == "POST":
        city.delete()
        messages.success(request, 'you have deleted the selected item!')
        return redirect('index')
    context = {'form': city}
    return render(request, '', context)

# #  to get the method i am redirecting the user to .
# from django.urls import reverse
# # this urlencode method is used to handle special charachters in urls ... to make it error free
# from urllib.parse import urlencode

# def some_view(request):
#     ...
    
#     base_url = reverse('product_view')  # 1 /products/
#     query_string =  urlencode({'category': category.id})  # 2 category=42
#     url = '{}?{}'.format(base_url, query_string)  # 3 /products/?category=42
#     return redirect(url)  # 4

# def product_view(request):
#     category_id = request.GET.get('category')  # 5