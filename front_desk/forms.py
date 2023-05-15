from django import forms
from .models import Guest, Room, Reservation, Invoice, HousekeepingTask, MaintenanceRequest, Inventory

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ('name', 'address', 'phone_number', 'email', 'passport_id', 'date_of_birth', 'nationality', 'loyalty_status')


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_number', 'floor_number', 'room_type', 'max_occupancy', 'view_type', 'room_status']
        labels = {
            'room_number': 'Room Number',
            'floor_number': 'Floor Number',
            'room_type': 'Room Type',
            'max_occupancy': 'Max Occupancy',
            'view_type': 'View Type',
            'room_status': 'Room Status',
        }
        widgets = {
            'room_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'floor_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'room_type': forms.TextInput(attrs={'class': 'form-control'}),
            'max_occupancy': forms.NumberInput(attrs={'class': 'form-control'}),
            'view_type': forms.TextInput(attrs={'class': 'form-control'}),
            'room_status': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['guest', 'room', 'check_in_date', 'check_out_date', 'num_of_guests', 'special_requests', 'payment_status']
        widgets = {
            'check_in_date': forms.DateInput(attrs={'type': 'date'}),
            'check_out_date': forms.DateInput(attrs={'type': 'date'}),
        }


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['guest', 'room', 'check_in_date', 'check_out_date', 'total_charge', 'tax_amount', 'payment_method', 'invoice_status']
        widgets = {
            'check_in_date': forms.DateInput(attrs={'type': 'date'}),
            'check_out_date': forms.DateInput(attrs={'type': 'date'}),
        }

class HousekeepingTaskForm(forms.ModelForm):
    class Meta:
        model = HousekeepingTask
        fields = ['room', 'task_description', 'task_status']
        widgets = {
            'task_description': forms.TextInput(attrs={'class': 'form-control'}),
            #'task_status': forms.Select(attrs={'class': 'form-control'}),
        }


class MaintenanceRequestForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRequest
        fields = ['room', 'request_description', 'request_status']

        widgets = {
            'room': forms.Select(attrs={'class': 'form-control'}),
            'request_description': forms.Textarea(attrs={'class': 'form-control'}),
            # 'request_status': forms.Select(attrs={'class': 'form-control'}),
        }

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['item_name', 'item_description', 'quantity', 'unit_price', 'reorder_level']


