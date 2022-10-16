from django.shortcuts import HttpResponse, render,redirect
# from booker.decorators import booker_only
# from bus_admin.decorators import bus_admin_only
# from system_admin.decorators import only_admins
# from customer.decorators import only_customer
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from booking.views import passengers
from . models import FinishPayment, PaymentInformation,PaymentMethod
# from . forms import PaymentMethodForm,PaidForm,PaymentInformationForm
from booker.models import SubRoute
from booking.models import Booking

# # Create your views here.

# # # ------------------------------------------------------------------------------------------------------|
# # #
# # #   MANAGE PAYMENT  METHODS
# # # ------------------------------------------------------------------------------------------------------|
# @login_required(login_url='login')
# @only_admins
# def payment_method(request):
#     payment_methods = PaymentMethod.objects.all()
#     context = {'payment_methods': payment_methods}
#     return render(request, 'payment/manage_payment_method.html', context)


# @login_required(login_url='login')
# @only_admins
# def add_payment_method(request):
#     form = PaymentMethodForm()
#     if request.method == "POST":
#         form = PaymentMethodForm(request.POST, request.FILES)
#         print(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('system_admin')
#         else:
#             messages.error(request, 'there is error in your input try again')
#     context = {'form': form}
#     return render(request, 'payment/new.html', context)


# @login_required(login_url='login')
# @only_admins
# def update_payment_method(request, id):
#     payment_method = PaymentMethod.objects.get(id=id)
#     form = PaymentMethodForm(instance=payment_method)
#     if request.method == "POST":
#         form = PaymentMethodForm(request.POST, request.FILES, instance=payment_method)
#         if form.is_valid():
#             form.save()
#             # success message
#             messages.success(request, ' updated successfully')
#             return redirect('system_admin')
#     context = {'form': form}
#     return render(request, 'payment/edit.html', context)


# @login_required(login_url='login')
# @only_admins
# def delete_payment_method(request, id):
#     payment_method = PaymentMethod(id=id)
#     if request.method == "POST":
#         payment_method.delete()
#         messages.success(request, 'you have deleted the selected item!')
#         return redirect('index')
#     context = {'form': payment_method}
#     return render(request, '', context)


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



@login_required(login_url='login')
# @only_customer
def pay(request, id):
    booking = Booking.objects.get(id=id)
    if request.method == 'POST':
        payment_information = PaymentInformation.objects.get(id=request.POST.get('py_id'))

        FinishPayment.objects.create(booking=booking,
        payment_information = payment_information,
        full_name=request.POST.get('full_name'),
        transaction_id = request.POST.get('transaction_id'),
        amount=request.POST.get('amount'))
        return redirect("passenger",pk=id)
        
    if booking.status != "waiting":
        messages.error(request, 'the this process  cannot accept payment ')
        # return redirect('booking')
    subroute = booking.bus_seat.first().subroute
    payment_information = PaymentInformation.objects.filter(subroute=subroute)
    print(payment_information)
    context = {'payment_informations': payment_information, 'price':booking.total_price}
    return render(request, 'payment/finish_payment.html', context)


# @login_required(login_url='login')
# @booker_only
# def manage_payment_information(request,q):
#     subroute = request.user.sub_route_set.filter(id=q)
#     payment_infos = PaymentInformation.objects.filter(subroute=subroute)
#     context = {"payment_infos":payment_infos,"subroute_id" : q}
#     return render(request,"payment/manage_payment_information.html",context)

# @login_required(login_url='login')
# @booker_only
# def add_payment_information(request,q):
#     form = PaymentInformationForm()
#     if request.method == 'POST':
#         form = PaymentInformationForm(request.POST)
#         if form.is_valid():
#             payment_info = form.save(commit=False)
#             payment_info.user = request.user
#             payment_info.subroute =  request.user.sub_route_set.filter(id=q)
#             payment_info.save()
#             messages.success(request, 'the operation is done successfully')
#             return redirect('manage_payment_info',q)
#         else:
#             messages.error(request, 'There is an error in your input')
#             return redirect('manage_payment_info',q)
#     context = {'form': form}
#     return render(request, 'payment/add_payment_information.html', context)

