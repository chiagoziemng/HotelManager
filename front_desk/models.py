from django.db import models
from django.utils import timezone

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
    AVAILABILITY_STATUS = (
        ('Available', 'Available'),
        ('Occupied', 'Occupied'),
        ('Maintenance', 'Maintenance'),
        ('Complimentary', 'Complimentary'),
    )
    room_number = models.IntegerField()
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    max_occupancy = models.IntegerField()
    room_price = models.FloatField()
    room_status = models.CharField(max_length=50, choices=ROOM_STATUS)
    availability = models.CharField(max_length=50, choices=AVAILABILITY_STATUS)
    MaintenanceRequest = models.CharField(max_length=255)


    def __str__(self):
        return str(self.room_number)



class Reservation(models.Model):
    CHECKING_STATUS = (
        ('Checked In', 'Checked In'),
        ('Checked Out', 'Checked Out'),
        ('No Show', 'No Show'),
    )
    EVENT_TYPES = (
        ('Reserve', 'Reserve'),
        ('Arriving', 'Arriving'),
        ('Staying Over', 'Staying Over'),
        ('Departing', 'Departing'),
    )
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    num_of_guests = models.IntegerField()
    checking = models.CharField(max_length=50, choices=CHECKING_STATUS)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    payment_status = models.CharField(max_length=50)
    total_charge = models.FloatField()
    payment_method = models.CharField(max_length=255)
    event_time = models.DateTimeField(default=timezone.now)
    days_left = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Reservation for {self.guest} - Room {self.room}"



