# Generated by Django 4.2.1 on 2023-05-19 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front_desk', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='loyalty_status',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='passport_id',
        ),
        migrations.RemoveField(
            model_name='room',
            name='floor_number',
        ),
        migrations.RemoveField(
            model_name='room',
            name='view_type',
        ),
        migrations.AddField(
            model_name='room',
            name='room_price',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('King', 'King'), ('Luxury', 'Luxury'), ('Normal', 'Normal'), ('Economic', 'Economic')], max_length=20),
        ),
    ]