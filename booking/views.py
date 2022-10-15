from django.shortcuts import render,HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Booking, Passanger
from booker.models import BusSeat, SubRoute
from bus_admin.models import SubRouteAdmin
from booker.decorators import booker_only
from django.contrib.auth.decorators import login_required




def booking(request, pk):
    sub_route = SubRoute.objects.get(id=pk)
    bus_seats = BusSeat.objects.filter(subroute=sub_route)
    if request.method=='POST':
        
        seats = request.POST.get('seats')
        seat_array = seats.split(',')
        seat_quantity = len(seat_array)
        price = request.POST.get('price')
        booking = Booking.objects.create(
            user=request.user,
                total_price=price,
                seat_quantity= seat_quantity)
        for seat in seat_array:
            reserve_seat = BusSeat.objects.get(id=seat)
            reserve_seat.reserved = True;
            booking.bus_seat.add(reserve_seat)
            booking.save()
            reserve_seat.save()
            """
             keed in mind before saving this is wanted to have name of each passanger i can make them fill out form
            afterward 
            """
        return redirect("pay",id=booking.id)


        

        # Booking.objects.create(
        # user=request.user,
        # sub_route=sub_route,
        # # bus=sub_route.bus,
        # # start=sub_route.start,
        # # destination=sub_route.destination,
        # # travel_date=sub_route.travel_date,
        # # travel_begin_time=sub_route.travel_begin_time,
        # travaler_name=request.POST['travaler_name'],
        # traveler_contact=request.POST['traveler_contact'],
        # seat_quantity=request.POST.get('seat_quantity'),)
        
        
        return redirect ('my-booking', pk=request.user.id)

    context={"bus_seats" : bus_seats}
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

def passengers(request,pk):
    booking = Booking.objects.get(id=pk)
    bus_seat = booking.bus_seat.all()
    if request.method=='POST':
       for seat in bus_seat:
        contact = request.POST.get(str(seat.id)) 
        name =request.POST.get(str(seat.seat_number)) 
        Passanger.objects.create(
            booking = booking,bus_seat=seat,name =name,contact = contact
        )
        return HttpResponse('everything is done now')

    context = {'seats': bus_seat}
    return render(request,'booking/passenger.html',context)  


