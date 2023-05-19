from django.db import models

class Guest(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    nationality = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Room(models.Model):
    ROOM_TYPES = (
        ('King', 'King'),
        ('Luxury', 'Luxury'),
        ('Normal', 'Normal'),
        ('Economic', 'Economic'),

    )
    ROOM_STATUS = (
        ('Clean', 'Clean'),
        ('Dirty', 'Dirty'),
        ('Turn Down', 'Turn Down'),
    )
    room_number = models.IntegerField()
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    max_occupancy = models.IntegerField()
    room_price = models.FloatField()
    room_status = models.CharField(max_length=50, choices=ROOM_STATUS)
    MaintenanceRequest = models.CharField(max_length=255)


    def __str__(self):
        return str(self.room_number)



class Reservation(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    num_of_guests = models.IntegerField()
    special_requests = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=50)

class Invoice(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_charge = models.DecimalField(max_digits=10, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    invoice_status = models.CharField(max_length=50)



