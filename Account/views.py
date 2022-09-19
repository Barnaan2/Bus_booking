from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from customer.decorators import only_customer
from bus_admin.decorators import bus_only
from booker.decorators import booker_only
from system_admin.decorators import allowed_users, superuser_only
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate, login, logout
from .forms import OurUserCreationForm,UserForm
from .models import User
from system_admin.models import BusBrand
from bus_admin.models import SubRouteAdmin

# from system_admin.models import Hotel


# ------------------------------------------------------------------------------------------------------|
#                                                                                   |
#   REGISTRATION AND USER MANAGEMENT
# ------------------------------------------------------------------------------------------------------|
def register(request):
    form = OurUserCreationForm()
    # This role should be assigned based on the place the request come  or by some hidden input field
    if request.method == 'POST':
        form = OurUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            context = {'form': form}
            return render(request, 'register.html', context)

    context = {'form': form}
    return render(request, 'account/login_register.html', context)


@never_cache
def login_page(request):
    # if user.is_authenticated:
    #     return HttpResponseRedirect(reverse('my_redirect'))
    if request.user.is_authenticated:
        if request.user.role == 'customer':
            return redirect('index')
        elif request.user.role == 'hotel_admin':
            return redirect('hotel')
        elif request.user.role == 'system_admin':
            return redirect('system_admin')
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
                return redirect('index')
            elif user.role == 'bus_admin':
                bus_brand = BusBrand.objects.filter(user=user).first()
                return redirect('bus_admin_home')
            elif user.role == 'booker':
                subroute_admin = SubRouteAdmin.objects.filter(user=user).first()
                # subroutes = SubRoute.objects.filter(subroute_admin=subroute_admin)
                # context = {'subroutes': subroutes}
                return redirect('subroute_home')
            elif user.role == 'system_admin':
                return redirect('system_admin')
            else:
                return HttpResponse('404 Page Not found')
        else:
            messages.error(request, 'Password is incorrect ')
            return redirect('login')
    page = "login"
    context = {"page": page}  
    return render(request, 'acccount/login_register.html', context )


# logout
def logout_page(request):
    logout(request)
    return redirect('index')


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