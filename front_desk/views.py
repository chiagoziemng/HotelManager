from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
# for checking and checkout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Guest, Room, Reservation
from .forms import GuestForm, RoomForm, ReservationForm


@csrf_exempt
def checkin(request, reservation_id):
    if request.method == 'POST':
        try:
            reservation = Reservation.objects.get(id=reservation_id)
            reservation.checking = 'Checked In'
            reservation.save()
            return JsonResponse({'status': 'success'})
        except Reservation.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Reservation not found'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@csrf_exempt
def checkout(request, reservation_id):
    if request.method == 'POST':
        try:
            reservation = Reservation.objects.get(id=reservation_id)
            reservation.checking = 'Checked Out'
            reservation.save()
            return JsonResponse({'status': 'success'})
        except Reservation.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Reservation not found'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


#Reservation  section

def reservation_list(request):
    reservations = Reservation.objects.all()
    for reservation in reservations:
        """
        we iterate over the reservations and 
        calculate the num_of_nights by subtracting the check_in_date from the check_out_date using the days attribute.
        """
        num_of_nights = (reservation.check_out_date - reservation.check_in_date).days + 1
        """
            we calculate the num_of_nights and current_night. The num_of_nights is the total number of nights for the reservation, 
            and the current_night is the number of nights elapsed from the check-in date until the current date.
        """
        current_night = (timezone.now().date() - reservation.check_in_date).days + 1
        reservation.num_of_nights = f"{current_night} of {num_of_nights} nights"

        if current_night == num_of_nights:
            reservation.event_type = "Departing"
        elif current_night > 1:
            reservation.event_type = "Staying Over"
            reservation.num_of_days_stayed = current_night - 1
        else:
            reservation.event_type = "Arriving"
    
    return render(request, 'reservation_list.html', {'reservations': reservations})

def reservation_detail(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    return render(request, 'reservation_detail.html', {'reservation': reservation})

def reservation_create(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)  # Create a reservation object without saving to the database yet
            num_of_days = (reservation.check_out_date - reservation.check_in_date).days
            reservation.total_charge = reservation.room.room_price * num_of_days
            reservation.save()  # Save the reservation with the calculated total_charge
            return redirect('reservation_detail', pk=reservation.pk)
    else:
        form = ReservationForm()
    return render(request, 'reservation_create.html', {'form': form})

def reservation_update(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservation_detail', pk=reservation.pk)
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'reservation_update.html', {'form': form, 'reservation': reservation})

def reservation_delete(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        reservation.delete()
        return redirect('reservation_list')
    return render(request, 'reservation_confirm_delete.html', {'reservation': reservation})

#Room section
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})

def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    return render(request, 'room_detail.html', {'room': room})

def room_create(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save()
            return redirect('room_detail', pk=room.pk)
    else:
        form = RoomForm()
    return render(request, 'room_create.html', {'form': form})

def room_update(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_detail', pk=room.pk)
    else:
        form = RoomForm(instance=room)
    return render(request, 'room_update.html', {'form': form, 'room': room})

def room_delete(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('room_list')
    return render(request, 'room_confirm_delete.html', {'room': room})



# Guest Section

def guest_list(request):
    guests = Guest.objects.all()
    return render(request, 'guest_list.html', {'guests': guests})

def guest_detail(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    return render(request, 'guest_detail.html', {'guest': guest})

def guest_create(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            guest = form.save()
            return redirect('guest_detail', pk=guest.pk)
    else:
        form = GuestForm()
    return render(request, 'guest_create.html', {'form': form})

def guest_update(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == 'POST':
        form = GuestForm(request.POST, instance=guest)
        if form.is_valid():
            guest = form.save()
            return redirect('guest_detail', pk=guest.pk)
    else:
        form = GuestForm(instance=guest)
    return render(request, 'guest_update.html', {'form': form})

def guest_delete(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == 'POST':
        guest.delete()
        return redirect('guest_list')
    return render(request, 'guest_confirm_delete.html', {'guest': guest})

