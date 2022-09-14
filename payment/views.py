from django.shortcuts import render,redirect
from django.contrib import messages
from booker.models import SubRoute
from django.contrib.auth.decorators import login_required
from . models import PaymentInformation,PaymentMethod
from . forms import PaymentMethodForm,PaidForm,PaymentInformationForm


# Create your views here.

# # ------------------------------------------------------------------------------------------------------|
# #
# #   MANAGE PAYMENT  METHODS
# # ------------------------------------------------------------------------------------------------------|
@login_required(login_url='login')
# @only_admins
def payment_method(request):
    payment_methods = PaymentMethod.objects.all()
    context = {'payment_methods': payment_methods}
    return render(request, 'payment_method/manage_payment_method.html', context)


@login_required(login_url='login')
# @only_admins
def add_payment_method(request):
    form = PaymentMethodForm()
    if request.method == "POST":
        form = PaymentMethodForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('system_admin')
        else:
            messages.error(request, 'there is error in your input try again')
    context = {'form': form}
    return render(request, 'payment/new.html', context)


@login_required(login_url='login')
# @only_admins
def update_payment_method(request, id):
    payment_method = PaymentMethod.objects.get(id=id)
    form = PaymentMethodForm(instance=payment_method)
    if request.method == "POST":
        form = PaymentMethodForm(request.POST, request.FILES, instance=payment_method)
        if form.is_valid():
            form.save()
            # success message
            messages.success(request, ' updated successfully')
            return redirect('system_admin')
    context = {'form': form}
    return render(request, 'payment/edit.html', context)


@login_required(login_url='login')
# @only_admins
def delete_payment_method(request, id):
    payment_method = PaymentMethod(id=id)
    if request.method == "POST":
        payment_method.delete()
        messages.success(request, 'you have deleted the selected item!')
        return redirect('index')
    context = {'form': payment_method}
    return render(request, '', context)


# ------------------------------------------------------------------------------------------------------|
#                                                                                                      |
#   CUSTOMER PAYMENT MANAGMENT
# ------------------------------------------------------------------------------------------------------|



# @login_required(login_url='login')
# @only_customer
# def payment_detail(request, br_id, pi_id):
#     form = PaidForm()
#     payment_details = PaymentInformation.objects.get(id=pi_id)
#     booking_request = BookingRequest.objects.get(id=br_id)
#     requested_rooms = RequestedRoom.objects.filter(booking_request=booking_request)
#     # booking = RequestedRoom.objects.filter(booking_request=booking_request)
#     # price = price_calculator(booking)
#     # for item in price:
#     #     if item['id'] == booking_request.id:
#     #         price = item['price']
#     if request.method == "POST":
#         form = PaidForm(request.POST, request.FILES)
#         if form.is_valid():
#             paid = form.save(commit=False)
#             paid.booking_request = booking_request
#             paid.payment_information = payment_details
#             paid.expected_payment = booking_request.price
#             paid.save()
#             booking_request.status = "paid"
#             booking_request.save()
#             messages.success(request, 'you have made the payment successfully')
#             context = {"payment_details": payment_details, "requested_rooms": requested_rooms,
#                        }
#             return redirect('mybooking')
#     context = {"booking_request": booking_request,"payment_details": payment_details, "requested_rooms": requested_rooms, 'form': form}
#     return render(request, 'customer/payment_detail.html', context)




# @login_required(login_url='login')
# # @only_customer
# def pay(request, id):
#     booking_request = BookingRequest.objects.get(id=id)
#     if booking_request.status != "make payment":
#         messages.error(request, 'the booking cannot accept payment ')
#         return redirect('booking')
#     # There may be many rooms under one Booking request . but all have the same hotel id
#     hotel = booking_request.hotel
#     payment_information = PaymentInformation.objects.filter(hotel=hotel)
#     # requested_rooms = RequestedRoom.objects.filter(booking_request=booking_request).first()
#     context = {'payment_information': payment_information, 'booking_request_id': booking_request.id}
#     return render(request, 'payment/pay.html', context)




@login_required(login_url='login')
# @hotel_only
def add_payment_information(request):
    form = PaymentInformationForm()
    subroute = request.user.sub_route_set.all().first()
    if request.method == 'POST':
        form = PaymentInformationForm(request.POST)
        if form.is_valid():
            payment_info = form.save(commit=False)
            payment_info.user = request.user
            payment_info.subroute = subroute
            payment_info.save()
            messages.success(request, 'the operation is done successfully')
            return redirect('hotel')
        else:
            messages.error(request, 'There is an error in your input')
            return redirect('index')
    context = {'form': form}
    return render(request, 'payment/add_payment_information.html', context)

