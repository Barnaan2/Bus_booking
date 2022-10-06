from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate, login, logout
from .forms import OurUserCreationForm,UserForm
from .models import User
from system_admin.models import BusBrand
from bus_admin.models import SubRouteAdmin
#  if you can help me to avoid this import i really appricate it
from bus_admin.views import add_booker
from urllib.parse import urlencode
from django.urls import reverse


# ------------------------------------------------------------------------------------------------------|
#                                                                                   
#   REGISTRATION AND USER MANAGEMENT
# ------------------------------------------------------------------------------------------------------|
def register(request,role="customer"):
    form = OurUserCreationForm()
    # This role should be assigned based on the place the request come  or by some hidden input field
    if request.user.is_authenticated:
        if request.user.role == 'customer':
            return HttpResponse("Error code 000003,you are already registered contact our customer service for help ..")
        elif request.user.role == 'bus_admin':
            role = "booker"
        elif request.user.role == 'booker':
            return HttpResponse("Error code 000003,you are already registered contact our customer service for help..")
        elif request.user.role == 'system_admin':
            role = "bus_admin"
        # elif request.user.is_superuser:
        #     role = "system_admin"
    if request.method == 'POST':
        form = OurUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if role == 'customer':
                login(request, user)
                return redirect('home')
            elif role == 'booker':
                base_url = reverse('add_booker')
                user = urlencode({'id':user.id})
                url = '{}?{}'.format(base_url,user)
                return redirect(url)
            elif role == "bus_admin":
                id = request.GET.get('id') 
                bus_brand = BusBrand.objects.get(id=id)
                bus_brand.user = user
                bus_brand.save()
                return redirect('manage_bus_brand')
            else:
                return HttpResponse("Error code 000004,you are already registered contact our customer service for help..")
      
        else:
            context = {'form': form,"role":role}
            return render(request, 'account/register.html', context)
    context = {"form":form,"role":role}
    return render(request, 'account/register.html', context)


@never_cache
def login_page(request):
    # if user.is_authenticated:
    #     return HttpResponseRedirect(reverse('my_redirect'))
    if request.user.is_authenticated:
        if request.user.role == 'customer':
            return redirect('home')
        elif request.user.role == 'bus_admin':
            return redirect('bus_admin_home')
        elif request.user.role == 'booker':
            return redirect('subroute_home')
        elif request.user.role == 'system_admin':
            return redirect('system_admin_index')
        else:
            return HttpResponse("Erorr code 000001,your account run into a problem. please contact customer survice...")
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)

        except:
            messages.error(request, 'Phone number does not exist')
            return redirect('login')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.role == 'customer':
                return redirect('home')
            elif user.role == 'bus_admin':
                bus_brand = BusBrand.objects.filter(user=user).first()
                return redirect('bus_admin_home')
            elif user.role == 'booker':
                subroute_admin = SubRouteAdmin.objects.filter(user=user).first()
                # subroutes = SubRoute.objects.filter(subroute_admin=subroute_admin)
                # context = {'subroutes': subroutes}
                return redirect('subroute_home')
            elif user.role == 'system_admin':
                return redirect('system_admin_index')
            else:
                return HttpResponse('404 Page Not found')
        else:
            messages.error(request, 'Password is incorrect ')
            return redirect('login')
    
 
    return render(request, 'account/login.html')


# logout
def logout_page(request):
    logout(request)
    return redirect('home')


# ------------------------------------------------------------------------------------------------------|
#                                                                                                      |
#   PROFILE MANAGMENT this gonna be a little bit confusing then the hotel
# ------------------------------------------------------------------------------------------------------|
#  A page for profile
@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid:
            form.save()
            return redirect('profile')
    return render(request, 'account/userprofile.html')


# FOR ADMINS