from django.shortcuts import render, redirect
from django.http import HttpResponse
from account.models import User
from bus_admin.models import SubRouteAdmin
from . models import SubRoute,BusSeat
from . decorators import booker_only
from . forms import SubRouteForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
@booker_only
def home(request):
    subroute_admin = SubRouteAdmin.objects.filter(user=request.user).first()
    subroutes = SubRoute.objects.filter(subroute_admin=subroute_admin)
    context = {'subroutes': subroutes}
    return render(request, 'booker/home.html')





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
    subroute_admin = SubRouteAdmin.objects.get(user=request.user)
    subroute = SubRoute.objects.filter(subroute_admin=subroute_admin)
    # q=request.GET.get('q') if request.GET.get('q') != None else ''
    # subroute=SubRoute.objects.filter(id=q)
    context = {"subroutes":subroute}
    return render(request,'booker/manage_subroute.html',context)



def add_subroute(request):
    form = SubRouteForm()
    subroute_admin = SubRouteAdmin.objects.filter(user=request.user).first()
    if request.method == "POST":
        form = SubRouteForm(request.POST)
        if form.is_valid():
           subroute =  form.save(commit=False)
           subroute.subroute_admin = subroute_admin
           subroute.route = subroute_admin.route
           subroute.start = subroute_admin.admin_at_city
           subroute.save()
           print(subroute)
           price = subroute_admin.route.single_seat_price
           number_of_seats = subroute.bus.number_of_seats

           activate_bus_seat(price,number_of_seats,subroute)
           return redirect("subroute_home")
    context = {'form':form}
    return render(request,'booker/new.html',context)

def update_subroute(request,id):
    subroute = SubRoute.objects.get(id=id)
    form = SubRouteForm(instance = subroute)
    if request.method == "POST":
        form = SubRouteForm(request.POST,instance=subroute)
        if form.is_valid():
            form.save()
        return redirect("subroute_home")
    context = {'form':form}
    return render(request,'booker/update.html',context)


def delete_subroute(request,id):
      subroute = SubRoute.objects.filter(id=id)
      if request.method == "POST":
            subroute.delete()
            return redirect("subroute_home")
      context = {'subroute':subroute}
      return render(request,' ',context)

def activate_bus_seat(price,number_of_seats,subroute):
    bus_seat_no = number_of_seats
    i = 0
    while(i<bus_seat_no):
        BusSeat.objects.create(subroute=subroute,price=price,seat_number = i+1)
        i +=1


    