# Generated by Django 4.2.1 on 2023-05-14 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('passport_id', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField()),
                ('nationality', models.CharField(max_length=50)),
                ('loyalty_status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=255)),
                ('item_description', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('reorder_level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField()),
                ('floor_number', models.IntegerField()),
                ('room_type', models.CharField(max_length=20)),
                ('max_occupancy', models.IntegerField()),
                ('view_type', models.CharField(max_length=50)),
                ('room_status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('num_of_guests', models.IntegerField()),
                ('special_requests', models.CharField(max_length=255)),
                ('payment_status', models.CharField(max_length=50)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front_desk.guest')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front_desk.room')),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_description', models.CharField(max_length=255)),
                ('request_status', models.CharField(max_length=50)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front_desk.room')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('total_charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tax_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(max_length=50)),
                ('invoice_status', models.CharField(max_length=50)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front_desk.guest')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front_desk.room')),
            ],
        ),
        migrations.CreateModel(
            name='HousekeepingTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_description', models.CharField(max_length=255)),
                ('task_status', models.CharField(max_length=50)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front_desk.room')),
            ],
        ),
    ]
