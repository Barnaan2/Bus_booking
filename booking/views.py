from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from .models import Booking
from booker.models import SubRoute
# Create your views here.


def booking(request, pk):
    sub_route = get_object_or_404(SubRoute, id=pk)
    if request.method=='POST':
    
        book=Booking.objects.create(
        user=request.user,
        sub_route=sub_route,
        bus=sub_route.bus,
        start=sub_route.start,
        destination=sub_route.destination,
        travel_date=sub_route.travel_date,
        travel_begin_time=sub_route.travel_begin_time,
        travaler_name=request.POST['travaler_name'],
        traveler_contact=request.POST['traveler_contact'],
        seat_quantity=request.POST.get('seat_quantity'),
        
        )
        return redirect ('my-booking', pk=request.user.id)
    
    context={}
    return render(request, 'booking/booking.html', context)