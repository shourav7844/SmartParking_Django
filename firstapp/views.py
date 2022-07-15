from asyncio.windows_events import NULL
from ctypes.wintypes import LGRPID
from email import message
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CustomerForm, PostForm, SignUpForm
from .models import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from . import models
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required
from json import dumps
from .models import *
import numpy

# for arduino
import serial
import time
from datetime import datetime



x = datetime.now

# Create your views here.

################  Brand New ###############
# Create your views here.
from .models import *
from .forms import CreateUserForm
from .decorators import unauthenticated_admin, unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group


def firstPageFinal(request):
	return render(request, 'firstPageBothFinal.html')


#########////////   Start : Admin Section ///////////##############
@unauthenticated_admin
def LandingPage_Admin(request):
	return render(request, 'LandingPage_Admin.html')

@unauthenticated_admin
def SignUp_Admin(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='admin')
			user.groups.add(group)

			messages.success(request, 'Account was created for ' + username)

			return redirect('SignIn_Admin')
		
	context = {'form':form}
	return render(request, 'Admin_SignUp.html', context)

@unauthenticated_admin
def SignIn_Admin(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')
		if User.objects.filter(username__exact=username).exists():
			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('Dashboard')
			else:
				messages.warning(request, 'password is incorrect')
		else:
			messages.warning(request, 'Username  is incorrect')

	context = {}
	return render(request, 'Admin_SignIn.html', context)

@login_required(login_url='SignIn_Admin')
@allowed_users(allowed_roles=['admin'])
def logoutAdmin(request):
	auth.logout(request)
	return HttpResponseRedirect('/SignIn_Admin')

@login_required(login_url='SignIn_Admin')
@allowed_users(allowed_roles=['admin'])
def Dashboard(request):
	context = {
		'name':request.user
		}
	return render(request, 'Dashboard.html', context)


@login_required(login_url='SignIn_Admin')
@allowed_users(allowed_roles=['admin'])
def Send_SlotStatus(request):
	# create data dictionary
	slot1=vehicleStatus.objects.get(slot='Slot 1')
	numberslot1 = slot1.veh_number
	statusSlot1=slot1.status

	slot2=vehicleStatus.objects.get(slot='Slot 2')
	numberslot2 = slot2.veh_number
	statusSlot2=slot2.status

	slot3=vehicleStatus.objects.get(slot='Slot 3')
	numberslot3 = slot3.veh_number
	statusSlot3=slot3.status

	slot4=vehicleStatus.objects.get(slot='Slot 4')
	numberslot4 = slot4.veh_number
	statusSlot4=slot4.status

	slot5=vehicleStatus.objects.get(slot='Slot 5')
	numberslot5 = slot5.veh_number
	statusSlot5=slot5.status

	slot6=vehicleStatus.objects.get(slot='Slot 6')
	numberslot6 = slot6.veh_number
	statusSlot6=slot6.status

	slot7=vehicleStatus.objects.get(slot='Slot 7')
	numberslot7 = slot7.veh_number
	statusSlot7=slot7.status

	slot8=vehicleStatus.objects.get(slot='Slot 8')
	numberslot8 = slot8.veh_number
	statusSlot8=slot8.status

	slot9=vehicleStatus.objects.get(slot='Slot 9')
	numberslot9 = slot9.veh_number
	statusSlot9=slot9.status

	slot10=vehicleStatus.objects.get(slot='Slot 10')
	numberslot10 = slot10.veh_number
	statusSlot10=slot10.status

	slot11=vehicleStatus.objects.get(slot='Slot 11')
	numberslot11 = slot11.veh_number
	statusSlot11=slot11.status

	slot12=vehicleStatus.objects.get(slot='Slot 12')
	numberslot12 = slot12.veh_number
	statusSlot12=slot12.status


	
	slot_list = [slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12]
	for slot in slot_list:
		if slot.status == 0:
			break
			

# main
	dataSlot1 = dumps(statusSlot1)
	dataSlot2 = dumps(statusSlot2)
	dataSlot3 = dumps(statusSlot3)
	dataSlot4 = dumps(statusSlot4)
	dataSlot5 = dumps(statusSlot5)
	dataSlot6 = dumps(statusSlot6)
	dataSlot7 = dumps(statusSlot7)
	dataSlot8 = dumps(statusSlot8)
	dataSlot9 = dumps(statusSlot9)
	dataSlot10 = dumps(statusSlot10)
	dataSlot11 = dumps(statusSlot11)
	dataSlot12 = dumps(statusSlot12)

	context = {
		'name':request.user,
		'slot1': dataSlot1, 
		'slot2': dataSlot2, 
		'slot3': dataSlot3, 
		'slot4': dataSlot4,
		'slot5': dataSlot5, 
		'slot6': dataSlot6, 
		'slot7': dataSlot7, 
		'slot8': dataSlot8,
		'slot9': dataSlot9, 
		'slot10': dataSlot10, 
		'slot11': dataSlot11, 
		'slot12': dataSlot12,
		'number1':numberslot1,
		'number2':numberslot2,
		'number3':numberslot3,
		'number4':numberslot4,
		'number5':numberslot5,
		'number6':numberslot6,
		'number7':numberslot7,
		'number8':numberslot8,
		'number9':numberslot9,
		'number10':numberslot10,
		'number11':numberslot11,
		'number12':numberslot12,
		
		}
	return render(request, 'mistArena.html', context)

@login_required(login_url='SignIn_Admin')
@allowed_users(allowed_roles=['admin'])
def manualEntry(request):
	return render(request, 'manualEntry.html')

@login_required(login_url='SignIn_Admin')
@allowed_users(allowed_roles=['admin'])
def manualExit(request):
	return render(request, 'manualExit.html')


@login_required(login_url='SignIn_Admin')
@allowed_users(allowed_roles=['admin'])
def ManualEntry(request):
	if request.method == 'POST':
		data = request.POST.get('veh_number')
		InsertInDatabaseVariable = vehicleIn(veh_number=data)
		InsertInDatabaseVariable.save()  
		if Customer.objects.filter(veh_number__iexact=data).exists():
			slot_info = Customer.objects.get(veh_number=data)
			slot_username = slot_info.username
			slot_rfid_no = slot_info.rfid_no
			slot_description = slot_info.description
			slot_veh_info = slot_info.veh_info_file
			slot_email = slot_info.email
			slot_phone_no = slot_info.phone_no
			slot_office_address = slot_info.office_address

			context = {
			'data':data,
			'username':slot_username,
			'rfid_no':slot_rfid_no,
			'description':slot_description,
			'veh_pic_info':slot_veh_info,
			'email':slot_email,
			'phone_no':slot_phone_no,
			'office_address':slot_office_address
			}
			return render(request, 'qqqq.html', context)

		else:
			not_registered = '>>>This car is not registered !!!!'
			slot_username_blank = '---'
			slot_rfid_no_blank = '---'
			slot_description_blank = '---'
			slot_veh_info_blank = '---'
			slot_email = '---'
			slot_phone_no = '---'
			slot_office_address = '---'
			else_context = {
				'data':not_registered,
				'username':slot_username_blank,
				'rfid_no':slot_rfid_no_blank,
				'description':slot_description_blank,
				'veh_pic_info':slot_veh_info_blank,
				'email':slot_email,
				'phone_no':slot_phone_no,
				'office_address':slot_office_address
			}
			return render(request, 'qqqq.html', else_context)
	else:
		return render(request, 'manualEntry.html')
	

@login_required(login_url='SignIn_Admin')
@allowed_users(allowed_roles=['admin'])
def ManualExit(request):
	if request.method == "POST":
		data = request.POST.get('veh_number')
		InsertInDatabaseVariable = vehicleOut(veh_number=data)
		InsertInDatabaseVariable.save()  
		if Customer.objects.filter(veh_number__iexact=data).exists():
			slot_info = Customer.objects.get(veh_number=data)
			slot_username = slot_info.username
			slot_rfid_no = slot_info.rfid_no
			slot_description = slot_info.description
			slot_veh_info = slot_info.veh_info_file
			slot_email = slot_info.email
			slot_phone_no = slot_info.phone_no
			slot_office_address = slot_info.office_address

			context = {
			'data':data,
			'username':slot_username,
			'rfid_no':slot_rfid_no,
			'description':slot_description,
			'veh_pic_info':slot_veh_info,
			'email':slot_email,
			'phone_no':slot_phone_no,
			'office_address':slot_office_address
			}
			return render(request, 'qqqq.html', context)

		else:
			not_registered = '>>>This car is not registered !!!!'
			slot_username_blank = '---'
			slot_rfid_no_blank = '---'
			slot_description_blank = '---'
			slot_veh_info_blank = '---'
			slot_email = '---'
			slot_phone_no = '---'
			slot_office_address = '---'
			else_context = {
				'data':not_registered,
				'username':slot_username_blank,
				'rfid_no':slot_rfid_no_blank,
				'description':slot_description_blank,
				'veh_pic_info':slot_veh_info_blank,
				'email':slot_email,
				'phone_no':slot_phone_no,
				'office_address':slot_office_address
			}
			return render(request, 'qqqq.html', else_context)
	else:
		return render(request, 'manualExit.html')


# Remove all whitespace inside
def remove(string):
    return "".join(string.split())


# Vehcle entry function(new)
@login_required(login_url='SignIn_Admin')
@allowed_users(allowed_roles=['admin'])
def authentication(request):

	if request.method == 'POST':

		# Insert vehicle in Slots in vehicleStatus table
		slot1 = vehicleStatus.objects.get(slot="Slot 1")
		slot2 = vehicleStatus.objects.get(slot="Slot 2")
		slot3 = vehicleStatus.objects.get(slot='Slot 3')
		slot4 = vehicleStatus.objects.get(slot='Slot 4')


		if slot1.status and slot2.status and slot3.status and slot4.status == True:
			messages.error(request, message="Sorry, all slots are booked..")
			return redirect('/MistArena/')

		else:
		#Do your stuff ,calling whatever you want from set_gpio.py 
			import sqlite3

			try:
				conn = sqlite3.connect('db.sqlite')
				cursor = conn.cursor()
				print("Opened database successfully")
			except Exception as e:
				print("Error during connection: ", str(e))


			# LOAD THU VIEN VA MODUL CAN THIET
			import cv2
			import pytesseract
			import numpy
			#DOC HINH ANH - TACH HINH ANH NHAN DIEN
			cap = cv2.VideoCapture(0)
			# Bắt đầu một vòng lặp


			while(True):
				ret, frame = cap.read()
				gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
				thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
				cv2.putText(frame, "KHUNG BIEN SO", (40, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))
				# Tạo đường viền để theo dõi bien so
				contours, h = cv2.findContours(thresh, 1, 2)
				largest_rectangle = [0, 0]
				for cnt in contours:
					lenght = 0.01 * cv2.arcLength(cnt, True)
					approx = cv2.approxPolyDP(cnt, lenght, True)
					if len(approx) == 4:
						area = cv2.contourArea(cnt)
						if area > largest_rectangle[0]:
							largest_rectangle = [cv2.contourArea(cnt), cnt, approx]
				x, y, w, h = cv2.boundingRect(largest_rectangle[1])

				image = frame[y:y + h, x:x + w]
				cv2.drawContours(frame, [largest_rectangle[1]], 0, (0, 255, 0), 8)
				cropped = frame[y:y + h, x:x + w]
				cv2.putText(frame, "BIEN SO", (x, y),
							cv2.FONT_HERSHEY_SIMPLEX, 1.5,
							(0, 0, 255))
				cv2.imshow('Dinh Vi Bien So Xe', frame)
				cv2.drawContours(frame, [largest_rectangle[1]], 0, (255, 255, 255), 18)
				# DOC HINH ANH CHUYEN THANH FILE TEXT
				pytesseract.pytesseract.tesseract_cmd = 'C:/Users/User/AppData/Local/Tesseract-OCR/tesseract.exe'
				gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
				blur = cv2.GaussianBlur(gray, (3, 3), 0)
				thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
				cv2.imshow('Bien So La', thresh)
				kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
				opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
				invert = 255 - opening
				dataOriginal = pytesseract.image_to_string(invert, lang='ben', config='--psm 6')

				data_space_remove = dataOriginal.strip()
				#data_arr = numpy.array(data_space_remove)
				
				string_data = numpy.char.strip(data_space_remove, chars="*!_[]-`~|\/.>,<?")
				data_=str(string_data)
				data=remove(data_)
				
				



				print("Bien so xe la:")
				print(data)

				key = cv2.waitKey(1650)
				if key == ord('0'):

					# cv2.imwrite(filename='saved_img.jpg', img=frame)
					# img_new = cv2.imread('saved_img.jpg')
					# cv2.waitKey(10)
					# cv2.destroyAllWindows()
					# img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)



					break
			fh = open('numbers.txt', 'w', encoding='utf-8')
			fh.write(data)
			fh.close()
			cap.release()
			cv2.destroyAllWindows()

			InsertIn_vehicleIn = vehicleIn(veh_number=data)  # 'data' is obtained from the video capture
			InsertIn_vehicleIn.save()
			# Detecting whether the vehicle number is registered or not
		if Customer.objects.filter(veh_number__iexact=data).exists():
			slot_info = Customer.objects.get(veh_number=data)
			slot_username = slot_info.username
			slot_rfid_no = slot_info.rfid_no
			slot_description = slot_info.description
			slot_veh_info = slot_info.veh_info_file
			slot_email = slot_info.email
			slot_phone_no = slot_info.phone_no
			slot_office_address = slot_info.office_address

			context = {
			'data':data,
			'username':slot_username,
			'rfid_no':slot_rfid_no,
			'description':slot_description,
			'veh_pic_info':slot_veh_info,
			'email':slot_email,
			'phone_no':slot_phone_no,
			'office_address':slot_office_address
			}
			return render(request, 'qqqq.html', context)

		else:
			not_registered = '>>>This car is not registered !!!!'
			slot_username_blank = '---'
			slot_rfid_no_blank = '---'
			slot_description_blank = '---'
			slot_veh_info_blank = '---'
			slot_email = '---'
			slot_phone_no = '---'
			slot_office_address = '---'
			else_context = {
				'data':not_registered,
				'username':slot_username_blank,
				'rfid_no':slot_rfid_no_blank,
				'description':slot_description_blank,
				'veh_pic_info':slot_veh_info_blank,
				'email':slot_email,
				'phone_no':slot_phone_no,
				'office_address':slot_office_address
			}
			return render(request, 'qqqq.html', else_context)

	else:
		return HttpResponseRedirect('/Dashboard/')


# Vehcle exit function(later)
@login_required(login_url='SignIn_Admin')
@allowed_users(allowed_roles=['admin'])
def authenticationOut(request):

	if request.method == 'POST':

		# Insert vehicle in Slots in vehicleStatus table
		slot1 = vehicleStatus.objects.get(slot="Slot 1")
		slot2 = vehicleStatus.objects.get(slot="Slot 2")
		slot3 = vehicleStatus.objects.get(slot='Slot 3')
		slot4 = vehicleStatus.objects.get(slot='Slot 4')


		if slot1.status and slot2.status and slot3.status and slot4.status == True:
			messages.error(request, message="Sorry, all slots are booked..")
			return redirect('/MistArena/')

		else:
		#Do your stuff ,calling whatever you want from set_gpio.py 
			import sqlite3

			try:
				conn = sqlite3.connect('db.sqlite')
				cursor = conn.cursor()
				print("Opened database successfully")
			except Exception as e:
				print("Error during connection: ", str(e))


			# LOAD THU VIEN VA MODUL CAN THIET
			import cv2
			import pytesseract
			import numpy
			#DOC HINH ANH - TACH HINH ANH NHAN DIEN
			cap = cv2.VideoCapture(0)
			# Bắt đầu một vòng lặp


			while(True):
				ret, frame = cap.read()
				gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
				thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
				cv2.putText(frame, "KHUNG BIEN SO", (40, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))
				# Tạo đường viền để theo dõi bien so
				contours, h = cv2.findContours(thresh, 1, 2)
				largest_rectangle = [0, 0]
				for cnt in contours:
					lenght = 0.01 * cv2.arcLength(cnt, True)
					approx = cv2.approxPolyDP(cnt, lenght, True)
					if len(approx) == 4:
						area = cv2.contourArea(cnt)
						if area > largest_rectangle[0]:
							largest_rectangle = [cv2.contourArea(cnt), cnt, approx]
				x, y, w, h = cv2.boundingRect(largest_rectangle[1])

				image = frame[y:y + h, x:x + w]
				cv2.drawContours(frame, [largest_rectangle[1]], 0, (0, 255, 0), 8)
				cropped = frame[y:y + h, x:x + w]
				cv2.putText(frame, "BIEN SO", (x, y),
							cv2.FONT_HERSHEY_SIMPLEX, 1.5,
							(0, 0, 255))
				cv2.imshow('Dinh Vi Bien So Xe', frame)
				cv2.drawContours(frame, [largest_rectangle[1]], 0, (255, 255, 255), 18)
				# DOC HINH ANH CHUYEN THANH FILE TEXT
				pytesseract.pytesseract.tesseract_cmd = 'C:/Users/User/AppData/Local/Tesseract-OCR/tesseract.exe'
				gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
				blur = cv2.GaussianBlur(gray, (3, 3), 0)
				thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
				cv2.imshow('Bien So La', thresh)
				kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
				opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
				invert = 255 - opening
				dataOriginal = pytesseract.image_to_string(invert, lang='ben', config='--psm 6')

				data_space_remove = dataOriginal.strip()
				#data_arr = numpy.array(data_space_remove)
				
				string_data = numpy.char.strip(data_space_remove, chars="*!_[]-`~|\/.>,<?")
				data_=str(string_data)
				data=remove(data_)
				
				



				print("Bien so xe la:")
				print(data)

				key = cv2.waitKey(1650)
				if key == ord('0'):

					# cv2.imwrite(filename='saved_img.jpg', img=frame)
					# img_new = cv2.imread('saved_img.jpg')
					# cv2.waitKey(10)
					# cv2.destroyAllWindows()
					# img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)



					break
			fh = open('numbers.txt', 'w', encoding='utf-8')
			fh.write(data)
			fh.close()
			cap.release()
			cv2.destroyAllWindows()

			InsertIn_vehicleOut = vehicleOut(veh_number=data)
			InsertIn_vehicleOut.save()
			# Detecting whether the vehicle number is registered or not
		if Customer.objects.filter(veh_number__iexact=data).exists():
			slot_info = Customer.objects.get(veh_number=data)
			slot_username = slot_info.username
			slot_rfid_no = slot_info.rfid_no
			slot_description = slot_info.description
			slot_veh_info = slot_info.veh_info_file
			slot_email = slot_info.email
			slot_phone_no = slot_info.phone_no
			slot_office_address = slot_info.office_address

			context = {
			'data':data,
			'username':slot_username,
			'rfid_no':slot_rfid_no,
			'description':slot_description,
			'veh_pic_info':slot_veh_info,
			'email':slot_email,
			'phone_no':slot_phone_no,
			'office_address':slot_office_address
			}
			return render(request, 'qqqq.html', context)

		else:
			not_registered = '>>>This car is not registered !!!!'
			slot_username_blank = '---'
			slot_rfid_no_blank = '---'
			slot_description_blank = '---'
			slot_veh_info_blank = '---'
			slot_email = '---'
			slot_phone_no = '---'
			slot_office_address = '---'
			else_context = {
				'data':not_registered,
				'username':slot_username_blank,
				'rfid_no':slot_rfid_no_blank,
				'description':slot_description_blank,
				'veh_pic_info':slot_veh_info_blank,
				'email':slot_email,
				'phone_no':slot_phone_no,
				'office_address':slot_office_address
			}
			return render(request, 'qqqq.html', else_context)

	else:
		return HttpResponseRedirect('/Dashboard/')

@login_required(login_url='SignIn_Admin')
@allowed_users(allowed_roles=['admin'])
def userDB_registration_info(request):
	user = Customer.objects.all()
	return render(request, 'userDB_registration_info.html', {'Name':user, 'name':request.user })

@login_required(login_url='SignIn_Admin')
@allowed_users(allowed_roles=['admin'])
def vehicleInDB(request):
	user = vehicleIn.objects.all()
	return render(request, 'vehicleInDB.html', {'Name':user, 'name':request.user})

@login_required(login_url='SignIn_Admin')
@allowed_users(allowed_roles=['admin'])
def vehicleOutDB(request):
	user = vehicleOut.objects.all()
	return render(request, 'vehicleOutDB.html', {'Name':user, 'name':request.user})

@login_required(login_url='SignIn_Admin')
@allowed_users(allowed_roles=['admin'])
def vehicleStatusDB(request):
	user = vehicleStatus.objects.all()
	return render(request, 'vehicleStatusDB.html', {'Name':user, 'name':request.user})

#Fetching data of Admin Panel
@login_required(login_url='SignIn_Admin')
@allowed_users(allowed_roles=['admin'])
def send_slotStatus(request):
	if request.user.is_authenticated:
		# create data dictionary
		slot1=vehicleStatus.objects.get(slot='Slot 1')
		numberslot1 = slot1.veh_number
		statusSlot1=slot1.status

		slot2=vehicleStatus.objects.get(slot='Slot 2')
		numberslot2 = slot2.veh_number
		statusSlot2=slot2.status

		slot3=vehicleStatus.objects.get(slot='Slot 3')
		numberslot3 = slot3.veh_number
		statusSlot3=slot3.status

		slot4=vehicleStatus.objects.get(slot='Slot 4')
		numberslot4 = slot4.veh_number
		statusSlot4=slot4.status

		slot5=vehicleStatus.objects.get(slot='Slot 5')
		numberslot5 = slot5.veh_number
		statusSlot5=slot5.status

		slot6=vehicleStatus.objects.get(slot='Slot 6')
		numberslot6 = slot6.veh_number
		statusSlot6=slot6.status

		slot7=vehicleStatus.objects.get(slot='Slot 7')
		numberslot7 = slot7.veh_number
		statusSlot7=slot7.status

		slot8=vehicleStatus.objects.get(slot='Slot 8')
		numberslot8 = slot8.veh_number
		statusSlot8=slot8.status

		slot9=vehicleStatus.objects.get(slot='Slot 9')
		numberslot9 = slot9.veh_number
		statusSlot9=slot9.status

		slot10=vehicleStatus.objects.get(slot='Slot 10')
		numberslot10 = slot10.veh_number
		statusSlot10=slot10.status

		slot11=vehicleStatus.objects.get(slot='Slot 11')
		numberslot11 = slot11.veh_number
		statusSlot11=slot11.status

		slot12=vehicleStatus.objects.get(slot='Slot 12')
		numberslot12 = slot12.veh_number
		statusSlot12=slot12.status


		
		slot_list = [slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12]
		for slot in slot_list:
			if slot.status == 0:
				break
				

	# main
		dataSlot1 = dumps(statusSlot1)
		dataSlot2 = dumps(statusSlot2)
		dataSlot3 = dumps(statusSlot3)
		dataSlot4 = dumps(statusSlot4)
		dataSlot5 = dumps(statusSlot5)
		dataSlot6 = dumps(statusSlot6)
		dataSlot7 = dumps(statusSlot7)
		dataSlot8 = dumps(statusSlot8)
		dataSlot9 = dumps(statusSlot9)
		dataSlot10 = dumps(statusSlot10)
		dataSlot11 = dumps(statusSlot11)
		dataSlot12 = dumps(statusSlot12)

		context = {
			'name':request.user,
			'slot1': dataSlot1, 
			'slot2': dataSlot2, 
			'slot3': dataSlot3, 
			'slot4': dataSlot4,
			'slot5': dataSlot5, 
			'slot6': dataSlot6, 
			'slot7': dataSlot7, 
			'slot8': dataSlot8,
			'slot9': dataSlot9, 
			'slot10': dataSlot10, 
			'slot11': dataSlot11, 
			'slot12': dataSlot12,
			'number1':numberslot1,
			'number2':numberslot2,
			'number3':numberslot3,
			'number4':numberslot4,
			'number5':numberslot5,
			'number6':numberslot6,
			'number7':numberslot7,
			'number8':numberslot8,
			'number9':numberslot9,
			'number10':numberslot10,
			'number11':numberslot11,
			'number12':numberslot12,
			
		}
		return render(request, 'mistArena.html', context)
	return render(request, 'mistArena.html', context)

#########////////   End : Admin Section ///////////##############

#########////////   Start : User Section ///////////##############
@unauthenticated_user
def LandingPage_User(request):
	return render(request, 'LandingPage_User.html')

@unauthenticated_user
def SignUp_User(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='user')
			user.groups.add(group)

			messages.success(request, 'Account was created for ' + username)

			return redirect('SignIn_User')
		
	context = {'form':form}
	return render(request, 'mmmm.html', context)


@unauthenticated_user
def SignIn_User(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')
		#form = CreateUserForm(request.POST)
		if User.objects.filter(username__exact=username).exists():
			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('UserProfile')
			else:
				messages.info(request, 'Password is incorrect')
		else:
			messages.info(request, 'Username is incorrect')

	context = {}
	return render(request, 'nnnn.html', context)

@login_required(login_url='SignIn_User')
@allowed_users(allowed_roles=['user'])
def logoutUser(request):
	auth.logout(request)
	return HttpResponseRedirect('/SignIn_User')

@login_required(login_url='SignIn_User')
@allowed_users(allowed_roles=['user'])
def UserProfile(request):
	return render(request, 'booking.html', {'date': x, 'name':request.user})

@login_required(login_url='SignIn_User')
@allowed_users(allowed_roles=['user'])
def Send_SlotStatus_User(request):
	# create data dictionary
	slot1=vehicleStatus.objects.get(slot='Slot 1')
	statusSlot1=slot1.status

	slot2=vehicleStatus.objects.get(slot='Slot 2')
	statusSlot2=slot2.status

	slot3=vehicleStatus.objects.get(slot='Slot 3')
	statusSlot3=slot3.status

	slot4=vehicleStatus.objects.get(slot='Slot 4')
	statusSlot4=slot4.status

	# main
	dataSlot1 = dumps(statusSlot1)
	dataSlot2 = dumps(statusSlot2)
	dataSlot3 = dumps(statusSlot3)
	dataSlot4 = dumps(statusSlot4)

	context = {
		'name':request.user,
		'slot1': dataSlot1, 
		'slot2': dataSlot2, 
		'slot3': dataSlot3, 
		'slot4': dataSlot4,
		'slot5': dataSlot1, 
		'slot6': dataSlot2, 
		'slot7': dataSlot3, 
		'slot8': dataSlot4,
		'slot9': dataSlot1, 
		'slot10': dataSlot2, 
		'slot11': dataSlot3, 
		'slot12': dataSlot4,
	}

	return render(request, 'layout.html', context)

@login_required(login_url='SignIn_User')
@allowed_users(allowed_roles=['user'])
def Customer_Input(request): 
	customer = request.user.customer
	form = CustomerForm(instance=customer)

	if request.method == 'POST':
		form = CustomerForm(request.POST, request.FILES, instance = customer)
		if form.is_valid():
			form.save()
	context = {'form' : form}
	return render(request, 'eeee.html', context)

#########////////   End : User Section ///////////##############