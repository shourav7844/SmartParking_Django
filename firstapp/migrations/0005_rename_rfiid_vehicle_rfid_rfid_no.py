# Generated by Django 4.0.4 on 2022-07-04 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_vehicle_rfid_delete_students'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle_rfid',
            old_name='rfiid',
            new_name='rfid_no',
        ),
    ]
