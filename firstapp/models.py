from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class registration(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, null=True, blank=True)
    password = models.CharField(max_length=32, null=True, blank=True)
    email_address = models.EmailField(max_length=60,null=True, blank=True, unique=True)#unique email address
    veh_number = models.CharField(max_length=32, null=True, blank=True, unique=True)#unique vehicle number

    class Meta:
        verbose_name = 'Registration'
        verbose_name_plural = 'Registration'
        ordering = ['email_address']
        db_table = 'registration'

    def __str__(self):
        return f"{self.name, self.email_address}"


class vehicleIn(models.Model):
    #veh_number = models.ForeignKey(registration, on_delete=models.DO_NOTHING)
    veh_number = models.CharField(max_length=12, null=True, blank=True)
    inTime = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = 'Vehicle In'
        verbose_name_plural = 'Vehicle Ins'
        #ordering = ['inTime']
        db_table = 'vehicleIn'

    def __str__(self):
        return f"{self.veh_number, self.inTime}"   
    
class vehicleOut(models.Model):
    veh_number = models.CharField(max_length=12, null=True, blank=True)
    outTime = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = 'Vehicle Out'
        verbose_name_plural = 'Vehicle Outs'
        #ordering = ['veh_number']
        db_table = 'vehicleOut'

    def __str__(self):
        return f"{self.veh_number}"


class vehicleStatus(models.Model):
    slot = models.CharField(max_length=20, null=True, blank=True)
    veh_number = models.CharField(max_length=12, null=True, blank=True, default='XXX')
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Vehicle Status'
        verbose_name_plural = 'Vehicle Status'
        ordering = ['slot']
        db_table = 'vehicleStatus'

    def __str__(self):
        return f"{self.slot}" f"{self.id}"

############### Brand New ###############

class vehicle_rfid(models.Model):
    username = models.CharField(max_length=30, null=True, blank=True)
    veh_number = models.CharField(max_length=30, null=True, blank=True)
    rfid_no = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Vehicle-Rfid'
        verbose_name_plural = 'Vehicle-Rfids'
        db_table = 'vehicle_rfid'

    def __str__(self):
        return f"{self.username, self.veh_number, self.rfid_no }" 


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=30, null=True, blank=True)
    veh_number = models.CharField(max_length=30, null=True, blank=True)
    rfid_no = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    veh_info_file = models.FileField(null=True, blank = True)
    office_address = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=30, null=True, blank=True)
    phone_no = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.username