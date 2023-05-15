from django.shortcuts import render, redirect, get_object_or_404
from .models import Guest, Room, Reservation, Invoice, HousekeepingTask, MaintenanceRequest, Inventory
from .forms import GuestForm, RoomForm, ReservationForm, InvoiceForm, HousekeepingTaskForm, MaintenanceRequestForm, InventoryForm

# Inventory section
def inventory_list(request):
    inventories = Inventory.objects.all()
    return render(request, 'inventory_list.html', {'inventories': inventories})

def inventory_detail(request, pk):
    inventory = Inventory.objects.get(pk=pk)
    return render(request, 'inventory_detail.html', {'inventory': inventory})

def inventory_create(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryForm()
    return render(request, 'inventory_create.html', {'form': form})

def inventory_update(request, pk):
    inventory = Inventory.objects.get(pk=pk)
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=inventory)
        if form.is_valid():
            form.save()
            return redirect('inventory_detail', pk=pk)
    else:
        form = InventoryForm(instance=inventory)
    return render(request, 'inventory_update.html', {'form': form, 'inventory': inventory})

def inventory_delete(request, pk):
    inventory = Inventory.objects.get(pk=pk)
    if request.method == 'POST':
        inventory.delete()
        return redirect('inventory_list')
    return render(request, 'inventory_confirm_delete.html', {'inventory': inventory})

# maintenance section
def maintenance_request_list(request):
    maintenance_requests = MaintenanceRequest.objects.all()
    return render(request, 'maintenance_request_list.html', {'maintenance_requests': maintenance_requests})

def maintenance_request_detail(request, pk):
    maintenance_request = get_object_or_404(MaintenanceRequest, pk=pk)
    return render(request, 'maintenance_request_detail.html', {'maintenance_request': maintenance_request})

def maintenance_request_create(request):
    if request.method == 'POST':
        form = MaintenanceRequestForm(request.POST)
        if form.is_valid():
            maintenance_request = form.save()
            return redirect('maintenance_request_detail', pk=maintenance_request.pk)
    else:
        form = MaintenanceRequestForm()
    return render(request, 'maintenance_request_create.html', {'form': form})

def maintenance_request_update(request, pk):
    maintenance_request = get_object_or_404(MaintenanceRequest, pk=pk)
    if request.method == 'POST':
        form = MaintenanceRequestForm(request.POST, instance=maintenance_request)
        if form.is_valid():
            maintenance_request = form.save()
            return redirect('maintenance_request_detail', pk=maintenance_request.pk)
    else:
        form = MaintenanceRequestForm(instance=maintenance_request)
    return render(request, 'maintenance_request_update.html', {'form': form, 'maintenance_request': maintenance_request})

def maintenance_request_delete(request, pk):
    maintenance_request = get_object_or_404(MaintenanceRequest, pk=pk)
    if request.method == 'POST':
        maintenance_request.delete()
        return redirect('maintenance_request_list')
    return render(request, 'maintenance_request_confirm_delete.html', {'maintenance_request': maintenance_request})

# HousekeepingTask section
def task_list(request):
    tasks = HousekeepingTask.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(HousekeepingTask, pk=pk)
    return render(request, 'task_detail.html', {'task': task})

def task_create(request):
    if request.method == 'POST':
        form = HousekeepingTaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = HousekeepingTaskForm()
    return render(request, 'task_create.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(HousekeepingTask, pk=pk)
    if request.method == 'POST':
        form = HousekeepingTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = HousekeepingTaskForm(instance=task)
    return render(request, 'task_update.html', {'form': form, 'task': task})

def task_delete(request, pk):
    task = get_object_or_404(HousekeepingTask, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'task_confirm_delete.html', {'task': task})

# invoice section
def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'invoice_list.html', {'invoices': invoices})

def invoice_detail(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    return render(request, 'invoice_detail.html', {'invoice': invoice})

def invoice_create(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save()
            return redirect('invoice_detail', pk=invoice.pk)
    else:
        form = InvoiceForm()
    return render(request, 'invoice_create.html', {'form': form})

def invoice_update(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            invoice = form.save()
            return redirect('invoice_detail', pk=invoice.pk)
    else:
        form = InvoiceForm(instance=invoice)
    return render(request, 'invoice_update.html', {'form': form, 'invoice': invoice})

def invoice_delete(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == 'POST':
        invoice.delete()
        return redirect('invoice_list')
    return render(request, 'invoice_confirm_delete.html', {'invoice': invoice})


#Reservation  section

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservation_list.html', {'reservations': reservations})

def reservation_detail(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    return render(request, 'reservation_detail.html', {'reservation': reservation})

def reservation_create(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
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
"""
    room_list: Displays a list of all rooms.
    room_detail: Shows the details of a specific room.
    room_create: Handles the creation of a new room.
    room_update: Handles updating an existing room.
    room_delete: Handles deleting a room.
"""

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

