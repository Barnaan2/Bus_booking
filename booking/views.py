
from django.shortcuts import render,HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Booking
from booker.models import SubRoute
from bus_admin.models import SubRouteAdmin
from booker.decorators import booker_only
# Create your views here.
from django.contrib.auth.decorators import login_required




def booking(request, pk):
    sub_route = get_object_or_404(SubRoute, id=pk)
    if request.method=='POST':
        Booking.objects.create(
        user=request.user,
        sub_route=sub_route,
        # bus=sub_route.bus,
        # start=sub_route.start,
        # destination=sub_route.destination,
        # travel_date=sub_route.travel_date,
        # travel_begin_time=sub_route.travel_begin_time,
        travaler_name=request.POST['travaler_name'],
        traveler_contact=request.POST['traveler_contact'],
        seat_quantity=request.POST.get('seat_quantity'),
        
        )
        return redirect ('my-booking', pk=request.user.id)

    context={}
    return render(request, 'booking/booking.html', context)
    
# ------------------------------------------------------------------------------------------------------|
#                                                                                   
#   MANAGE BOOKING 
# ------------------------------------------------------------------------------------------------------|
# @login_required(login_url='login')
# @booker_only
# def manage_booking(request):
#     subroute_admin = SubRouteAdmin.objects.filter(user=request.user).first()
#     booking_requests= Booking.objects.filter(sub_roure__subroute_admin =subroute_admin)
#     q=request.GET.get('q') 
#     if request.GET.get('q') != None:
#         sub_route=SubRoute.objects.get(id=q)
#         booking_request=sub_route.booking_set.all().order_by('-created') 
#         context={'booking_request':booking_request}
#         return render(request, 'booking/booking_request.html', context)
#     context={'booking_requests':booking_requests}
#     return render(request, 'booking/booking_request.html', context)

@login_required(login_url='login')
@booker_only
def manage_booking(request,pk):
    # finish_payment=FinishPayment.objects.filter()
    finish_payment = ""
    sub_route=SubRoute.objects.get(id=pk)
    subroute_admin = SubRouteAdmin.objects.filter(user=request.user).first()
    if subroute_admin in sub_route.subroute_admin: 
        booking_requests=sub_route.booking_set.all().order_by('-created') 
    else:
        return HttpResponse("Error code 000002; you are not allowed to access this page, please contant customer service ")
    context={'booking_requests':booking_requests}
    return render(request, 'booking/booking_request.html', context)

