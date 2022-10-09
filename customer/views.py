from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from account.models import User
from django.contrib.auth.forms import UserCreationForm
from booker.models import SubRoute, Route
from booking.models import Booking
from system_admin.models import BusBrand
### please do not import all classes from .models because there may be error while login

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    start =request.GET.get('x')
    destination = request.GET.get('y')
    date = request.GET.get('z')
    if request.GET.get('start') != None:
      routes=Route.objects.filter(

        Q(first_city__icontains=q) |
        Q(second_city__icontains=q) )
    else:
        routes = Route.objects.all()
    buses = BusBrand.objects.all();
    context={'routes':routes,'buses':buses}
    return render(request, 'customer/home.html', context)


def subRoute(request, pk):
    route=Route.objects.get(id=pk)
    sub_routes=route.subroute_set.all()

    context={'route':route, 'sub_routes':sub_routes}
    return render(request, 'customer/sub_route.html', context)


def myBooking(request, pk):
    user=User.objects.get(id=pk)
    bookings=user.booking_set.filter().order_by('-created')

    context={'bookings':bookings}
    return render(request, 'customer/my_booking.html', context)

# def pay(request, pk):
#     booking=Booking.objects.get(id=pk)
#     payment_infos=booking.route.paymentinformantion_set.all()

#     if request.method == 'POST':
#         finish_payment =FinishPayment.objects.create(
#         booking=booking,
#         payment_method_id=request.POST['payment_method'],
#         paid_by=request.POST['paid_by'],
#         transaction_id=request.POST['transaction_id'],
#         )
#         return redirect ('my-booking', pk=request.user.id)

#     context={'booking':booking, 'payment_infos':payment_infos}
#     return render(request, 'customer/pay.html', context)

# def loginPage(request):
#     page='login'
#     if request.method=='POST':
#         username=request.POST.get('username')
#         password=request.POST.get('password')

#         try:
#              user=User.objects.get(username=username)

#         except:
#             messages.error(request, 'Sorry! User does not exist.')
#         user=authenticate(request, username=username, password=password)

#         if user is not None:

#             login(request, user)
#             return redirect('home')
#         else :
#           messages.error(request, 'Sorry! username or password does not exist.')
#     context={'page':page}
#     return render(request, 'customer/login_register.html', context)


# def logoutUser(request):
#     logout(request)
#     return redirect('home')


# def registerPage(request):
#     page='register'
#     form=UserCreationForm()

#     if request.method =='POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             user.is_active = True
#             user.save()
#             return redirect('home')
#         else:
#             messages.error(request, "An error occured during registration")
#     context={'page':page, 'form':form}
#     return render(request, 'customer/login_register.html', context)
