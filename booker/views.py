from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from bus_admin.models import Route, SubRouteAdmin, SubRoute, SubRouteBusAdmin
from customer.models import Booking
from system_admin.models import BusAdmin
from .models import FinishPayment, FinishPaymentStatus
# Create your views here.



def home(request, pk):
    user=User.objects.get(id=pk)
    subroute_bus_admins=user.subroutebusadmin_set.filter()
    # subroute_bus=user.subroutebusadmin.subroute_bus.all()
    subroute_admins=user.subrouteadmin_set.filter()
    context={'user':user,  'subroute_admins':subroute_admins, 'subroute_bus_admins':subroute_bus_admins}
    
    if request.user != user:
           return HttpResponse("You are not allowed here!")
    return render(request, 'booker/home.html', context)

def bookingRequest(request, pk):
    sub_route=SubRoute.objects.get(id=pk)
    bookings=sub_route.booking_set.filter().order_by('-created') 
    finish_payment=FinishPayment.objects.filter()

    context={'sub_route':sub_route, 'bookings':bookings, 'finish_payment':finish_payment}

    return render(request, 'booker/booking_request.html', context)


def finishPaymentStatus(request, pk):
    finishpayment=FinishPayment.objects.get(booking_id=pk)
    bookings=Booking.objects.filter()

    if request.method == 'POST':
        status=FinishPaymentStatus.objects.create(
        fnishpayment=finishpayment,
        status=request.POST['status'],
       
        )
        return redirect ('home', pk=request.user.id)
   
    context={'bookings':bookings, 'finishpayment':finishpayment}
    # if request.user != finishpayment.booking.hotel.admin: 
    #        return HttpResponse("You are not allowed here!")
    return render(request, 'booker/paid_unpaid.html', context)