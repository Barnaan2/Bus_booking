from django.shortcuts import render, redirect
from django.http import HttpResponse
from account.models import User
from bus_admin.models import SubRouteAdmin
from . models import SubRoute 
from . forms import SubRouteForm




def home(request,pk):
    user=User.objects.get(id=pk)
    subroute_bus_admins=user.subroutebusadmin_set.filter()
    subroute_bus=user.subroutebusadmin.subroute_bus.all()
    subroute_admins=user.subrouteadmin_set.filter()
    context={'user':user,  'subroute_admins':subroute_admins}

    if request.user != user:
           return HttpResponse("You are not allowed here!")
    return render(request, 'booker/home.html')

def bookingRequest(request, pk):
    sub_route=SubRoute.objects.get(id=pk)
    bookings=sub_route.booking_set.filter().order_by('-created') 
    # finish_payment=FinishPayment.objects.filter()
    finish_payment = ""
    context={'sub_route':sub_route, 'bookings':bookings, 'finish_payment':finish_payment}
    return render(request, 'booker/booking_request.html', context)


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
    form = SubRouteForm()
    subroute_admin = SubRouteAdmin.objects.filter(user=request.user).first()
    if request.method == "POST":
        form = SubRouteForm(request.POST)
        if form.is_valid():
           subroute =  form.save(commit=False)
           subroute.subroute_admin = SubRouteAdmin.objects.filter(user=request.user).first()
           subroute.route = subroute_admin.route
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


    
        

 