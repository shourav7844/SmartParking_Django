from django import forms
from django.forms import ModelForm
from matplotlib import widgets
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError  



class PostForm(ModelForm):
	class Meta:
		model = registration
		fields = '__all__'


class Intimeform(forms.ModelForm):
	class Meta:
		model = vehicleIn
		fields = '__all__'

class Outtimeform(forms.ModelForm):
	class Meta:
		model = vehicleOut
		fields = '__all__'

class Statusform(forms.ModelForm):
	class Meta:
		model = vehicleStatus
		fields = '__all__'


class SignUpForm(UserCreationForm):
	password2 = forms.CharField(label='Confirm Password (again)',
	widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email']
		labels = {'email': 'Email'}



from django import forms  




############ Brand New ################


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		widgets = {}

	def username_clean(self):  
		username = self.cleaned_data['username'].lower()  
		new = User.objects.filter(username = username)  
		if new.count():  
			raise ValidationError("User Already Exist")  
		return username  

	def email_clean(self):  
		email = self.cleaned_data['email'].lower()  
		new = User.objects.filter(email=email)  
		if new.count():  
			raise ValidationError(" Email Already Exist")  
		return email  

	def clean_password2(self):  
		password1 = self.cleaned_data['password1']  
		password2 = self.cleaned_data['password2']  

		if password1 and password2 and password1 != password2:  
			raise ValidationError("Password don't match")  
		return password2  

	def save(self, commit = True):  
		user = User.objects.create_user(  
			self.cleaned_data['username'],  
			self.cleaned_data['email'],  
			self.cleaned_data['password1']  
		)  
		return user  

	######### Widget to customize css ########
	username = forms.CharField(widget=forms.TextInput(
		attrs={
		'class':'form-control',
		'id':'username',
		'placeholder':'Username'
		}
		))
	email = forms.CharField(widget=forms.EmailInput(
		attrs={
		'class':'form-control',
		'id':'email',
		'placeholder':'Email Address'
		}
		))
	password1 = forms.CharField(widget=forms.PasswordInput(
		attrs={
		'class':'form-control',
		'id':'password1',
		'placeholder':'Password'
		}
		))
	password2 = forms.CharField(widget=forms.PasswordInput(
		attrs={
		'class':'form-control',
		'id':'password2',
		'placeholder':'Re-type password'
		}
		))




class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']

	######### Widget to customize css ########
	username = forms.CharField(widget=forms.TextInput(
		attrs={
		'class':'form-control',
		'id':'username',
		'title':'Username'
		}
		))
	veh_number = forms.CharField(widget=forms.TextInput(
		attrs={
		'class':'form-control',
		'id':'veh_number'
		}
		))
	rfid_no = forms.CharField(widget=forms.TextInput(
		attrs={
		'class':'form-control',
		'id':'rfid_no'
		}
		))
	description = forms.CharField(widget=forms.Textarea(
		attrs={
		'class':'form-control',
		'id':'description',"rows":5, "cols":10
		}
		))
	veh_info_file = forms.FileField(widget=forms.ClearableFileInput(
		attrs={
		'class':'form-control',
		'id':'veh_info_file'
		}
		))
	email = forms.CharField(widget=forms.TextInput(
		attrs={
		'class':'form-control',
		'id':'email'
		}
		))	
	phone_no = forms.CharField(widget=forms.TextInput(
		attrs={
		'class':'form-control',
		'id':'phone_no'
		}
		))	
	office_address = forms.CharField(widget=forms.TextInput(
		attrs={
		'class':'form-control',
		'id':'office_address'
		}
		))
