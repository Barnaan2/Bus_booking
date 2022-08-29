from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from booker.models import SubRoute 
# from customer.models import Booking
from system_admin.models import BusAdmin,Route, SubRouteAdmin
# from .models import FinishPayment, FinishPaymentStatus
from .forms import SubRouteForm
# Create your views here.



def home(request):
    # user=User.objects.get(id=pk)
    # subroute_bus_admins=user.subroutebusadmin_set.filter()
    # subroute_bus=user.subroutebusadmin.subroute_bus.all()
    # subroute_admins=user.subrouteadmin_set.filter()
    # context={'user':user,  'subroute_admins':subroute_admins}

    # if request.user != user:
    #        return HttpResponse("You are not allowed here!")
    return render(request, 'booker/home.html')

# def bookingRequest(request, pk):
#     sub_route=SubRoute.objects.get(id=pk)
#     bookings=sub_route.booking_set.filter().order_by('-created') 
#     finish_payment=FinishPayment.objects.filter()

#     context={'sub_route':sub_route, 'bookings':bookings, 'finish_payment':finish_payment}

#     return render(request, 'booker/booking_request.html', context)


# def finishPaymentStatus(request, pk):
#     finishpayment=FinishPayment.objects.get(booking_id=pk)
#     bookings=Booking.objects.filter()

#     if request.method == 'POST':
#         status=FinishPaymentStatus.objects.create(
#         fnishpayment=finishpayment,
#         status=request.POST['status'],
       
#         )
#         return redirect ('home', pk=request.user.id)
   
#     context={'bookings':bookings, 'finishpayment':finishpayment}
#     # if request.user != finishpayment.booking.hotel.admin: 
#     #        return HttpResponse("You are not allowed here!")
#     return render(request, 'booker/paid_unpaid.html', context)

    # manage subroute
def manage_subroute(request):
    subroute = SubRoute.objects.filter(user=request.user)
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    subroute=SubRoute.objects.filter(id=q)
    context = {"subroute":subroute}
    return render(request,'booker/manage_subroute.html',context)



def add_subroute(request):
    subroute_admin = SubRouteAdmin.objects.filter(user=request.user).first()
    form = SubRouteForm()
    if request.method == "POST":
        form = SubRouteForm(request.POST)
        if form.is_valid():
           subroute =  form.save(commit=False)
           subroute.admin_at = subroute_admin.admin_at
           subroute.save()
           return redirect("subroute_home")
    context = {'form':form}
    return redirect(request,'booker/new.html',context)



def update_subroute(request,id):
    subroute = SubRoute.objects.filter(id=id)
    form = SubRouteForm(instance = subroute)
    if request.method == "POST":
        form = SubRouteForm(request.POST,instance=subroute)
        if form.is_valid():
            form.save()
        return redirect("subroute_home")
    context = {'form':form}
    return redirect(request,'booker/update.html',context)


def delete_subroute(request,id):
      subroute = SubRoute.objects.filter(id=id)
      if request.method == "POST":
            subroute.delete()
            return redirect("subroute_home")
      context = {'subroute':subroute}
      return redirect(request,' ',context)


    
        

 