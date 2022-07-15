from django.contrib import admin
from .models import *
from .forms import *
# Register your models here.

# @admin.register(registration)
class Registration(admin.ModelAdmin):
    list_display = ['user_id', 'name', 'veh_number']
    # readonly_fields = ('user_id',)
    form = PostForm

class VehicleIn(admin.ModelAdmin):
    list_display = ['veh_number', 'inTime']
    readonly_fields = ('inTime',)
    form = Intimeform

class VehicleOut(admin.ModelAdmin):
    list_display = ['veh_number', 'outTime']
    readonly_fields = ('outTime',)
    form = Outtimeform

class VehicleStatus(admin.ModelAdmin):
    list_display = ['slot', 'veh_number', 'status']
    readonly_fields = ('status',)
    form = Statusform

class Vehicle_rfid(admin.ModelAdmin):
    list_display = ['username', 'veh_number', 'rfid_no']



# class VehicleInOut(admin.ModelAdmin):
#     list_display = ['veh_number', 'inTime','outTime', 'totalTime']
#     readonly_fields = ('inTime','outTime', 'totalTime')
#     form = InOutform

# class vehicleIn(admin.ModelAdmin):
#     readonly_fields = ('inTime',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'username', 'veh_number', 'rfid_no', 'description', 'veh_info_file']


admin.site.register(registration)

admin.site.register(vehicleIn, VehicleIn)

admin.site.register(vehicleOut, VehicleOut)

admin.site.register(vehicleStatus, VehicleStatus)

admin.site.register(vehicle_rfid, Vehicle_rfid)




