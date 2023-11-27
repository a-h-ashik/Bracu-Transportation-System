from django.shortcuts import render, redirect
from user.models import User
from .models import Buses, Tickets

# Create your views here.
def interface(request, id):
    user = User.objects.filter(user_id=id).first()
    buses = Buses.objects.all()
    return render(request, 'ticket_booking/chart_interface.html', {'buses':buses, 'user':user})

def seating_cart(request, id, bus_number):
    user = User.objects.filter(user_id=id).first()
    general_seats = {}
    for i in range(1, 15):
        if i < 10:
            key = f'G0{i}'
        else:
            key = f'G{i}'

        seats = Tickets.objects.filter(bus_number=bus_number)
        booked = seats.filter(seat_number=key).exists()
        if booked:
            general_seats[key] = {'booked': True}
        else:
            general_seats[key] = {'booked': False}


    return render(request, 'ticket_booking/seating_cart.html', {'user':user, 'general_seats':general_seats, 'bus_number':bus_number})


def booking_form(request, id, bus_number, seat_number):
    user = User.objects.filter(user_id=id).first()
    general_seats = {}
    for i in range(1, 15):
        if i < 10:
            key = f'G0{i}'
        else:
            key = f'G{i}'

        booked = Tickets.objects.filter(seat_number=key).exists()
        if booked:
            general_seats[key] = {'booked': True}
        else:
            general_seats[key] = {'booked': False}

    if request.method == 'POST':
        seat = request.POST.get('seat')
        count = Tickets.objects.all().count()
        ticket_id = f'T{count+1}'
        instance = Tickets(ticket_id=ticket_id, bus_number=bus_number, seat_number=seat, user_id=user.user_id)
        instance.save()
        
        new_point = user.point - 50
        user.point = new_point
        user.save()

        return redirect('cart', id=user.user_id, bus_number=bus_number)


    return render(request, 'ticket_booking/booking_form.html', {'user':user, 'general_seats':general_seats, 'bus_number':bus_number, 'seat_number':seat_number})
    


