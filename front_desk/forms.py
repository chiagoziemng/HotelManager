from django import forms
from .models import Guest, Room, Reservation, Invoice

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ('name', 'address', 'phone_number', 'email', 'nationality')


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_number','room_type', 'max_occupancy', 'room_price', 'room_status']
        labels = {
            'room_number': 'Room Number',
            'room_type': 'Room Type',
            'max_occupancy': 'Max Occupancy',
            'room_price': 'Room Price',
            'room_status': 'Room Status',
        }
        widgets = {
            'room_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'room_type': forms.Select(attrs={'class': 'form-control'}),
            'max_occupancy': forms.NumberInput(attrs={'class': 'form-control'}),
            'room_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'room_status': forms.Select(attrs={'class': 'form-control'}),
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



