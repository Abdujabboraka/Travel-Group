from django.shortcuts import render, redirect
from .models import Destination, Review, User, Booking
# Create your views here.

def homepage(request):
    context ={
        'destinations': Destination.objects.all(),
        'users': User.objects.all(),
        'bookings': Booking.objects.all(),
        'title': "Bosh Sahifa"
    }
    return render(request, 'index.html', context)

def destination_detail(request, d_id):
    destination = Destination.objects.get(id=d_id)
    context = {
        'destination': destination,
        'title': f"{destination.name} Detayları"
    }
    return render(request, 'detail.html', context)

def booking(request):
    booking = Booking.objects.all()
    destinations = Destination.objects.all()
    context = {'bookings': booking, 'destinations': destinations}
    if request.method == 'POST':
        return redirect('homepage')
    return render(request, 'booking.html', context)