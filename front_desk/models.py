from django.db import models

class Guest(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    passport_id = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=50)
    loyalty_status = models.CharField(max_length=50)

class Room(models.Model):
    room_number = models.IntegerField()
    floor_number = models.IntegerField()
    room_type = models.CharField(max_length=20)
    max_occupancy = models.IntegerField()
    view_type = models.CharField(max_length=50)
    room_status = models.CharField(max_length=50)

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

class HousekeepingTask(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    task_description = models.CharField(max_length=255)
    task_status = models.CharField(max_length=50)

class MaintenanceRequest(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    request_description = models.CharField(max_length=255)
    request_status = models.CharField(max_length=50)

class Inventory(models.Model):
    item_name = models.CharField(max_length=255)
    item_description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    reorder_level = models.IntegerField()

