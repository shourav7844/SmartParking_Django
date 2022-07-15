from django.urls import path
from . import views


urlpatterns = [

###################  Brand New  ########################
	path('', views.firstPageFinal, name='firstPageBothFinal'),

	###################  Start: Admin Section  ########################
	path('LandingPage_Admin/', views.LandingPage_Admin, name='LandingPage_Admin'),
	path('SignUp_Admin/', views.SignUp_Admin, name='SignUp_Admin'),
	path('SignIn_Admin/', views.SignIn_Admin, name='SignIn_Admin'),
	path('logoutAdmin/', views.logoutAdmin, name="logoutAdmin"),
	path('Dashboard/', views.Dashboard, name='Dashboard'),
	path('MistArena/',views.Send_SlotStatus , name='MistArena'),
	path('ManualEntry/', views.ManualEntry, name='ManualEntry'),
	path('ManualExit/', views.ManualExit, name='ManualExit'),
	path('manualEntry/', views.manualEntry, name='manualEntry'),
	path('manualExit/', views.manualExit, name='manualExit'),
	path('userDB_registration_info/',views.userDB_registration_info , name='userDB_registration_info'),
	path('vehicleInDB/',views.vehicleInDB , name='vehicleInDB'),
	path('vehicleOutDB/',views.vehicleOutDB , name='vehicleOutDB'),
	path('vehicleStatusDB/',views.vehicleStatusDB , name='vehicleStatusDB'),
	path('entryAuthentication/', views.authentication, name='entryAuthentication'),
	path('register/', views.authenticationOut, name='exitAuthentication'),

	###################  End: Admin Section  ########################

	###################  Start: User Section  ########################
	path('LandingPage_User/', views.LandingPage_User, name='LandingPage_User'),
	path('SignUp_User/', views.SignUp_User, name='SignUp_User'),
	path('SignIn_User/', views.SignIn_User, name='SignIn_User'),
	path('logoutUser/', views.logoutUser, name="logoutUser"),
	path('UserProfile/', views.UserProfile, name='UserProfile'),
	path('MistArena_User/',views.Send_SlotStatus_User , name='MistArena_User'),
	path('Customer_Input/', views.Customer_Input, name='Customer_Input'),

	###################  End: User Section  ########################
]