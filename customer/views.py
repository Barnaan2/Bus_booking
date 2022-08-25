from django.shortcuts import render, redirect
from django.contrib import messages
from Account.models import User
### please do not import all classes from .models because there may be error while login

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from Account.forms import UserRegisterForm
# Create your views here.

def home(request):
    context={}
    return render(request, 'customer/home.html', context)


def loginPage(request):
    page='login'
    if request.method=='POST':
        phone_number=request.POST.get('phone_number')
        password=request.POST.get('password')

        try:
             user=User.objects.get(phone_number=phone_number)
           
        except:
            messages.error(request, 'Sorry! User does not exist.')
        user=authenticate(request, phone_number=phone_number, password=password)
        
        if user is not None:
           
            login(request, user)
            return redirect('home')
        else :
          messages.error(request, 'Sorry! phone number or password does not exist.')  
    context={'page':page}
    return render(request, 'customer/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    page='register'
    form=UserRegisterForm()
    
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.is_active = True
            user.save()
            return redirect('home')
        else:
            messages.error(request, "An error occured during registration")
    context={'page':page, 'form':form}
    return render(request, 'customer/login_register.html', context)