# bookings/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from destinations.models import Destination
from .forms import BookingForm
from django.contrib.auth.decorators import login_required

@login_required
def create_booking(request, destination_id):
    destination = get_object_or_404(Destination, id=destination_id)
    
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.destination = destination
            booking.save()
            return redirect('home')
    else:
        form = BookingForm()
    
    context = {
        'form': form,
        'destination': destination,
    }
    return render(request, 'create_booking.html', context)

def booking_page(request):
    return render(request, 'templates/booking_page.html')