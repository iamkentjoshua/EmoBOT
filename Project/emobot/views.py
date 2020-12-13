from django.http import HttpResponse
from django.http import Http404
from datetime import datetime
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from .forms import CreateUserForm, PersonForm
from .models import Person
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here. Arrange Views in alphabetical order

# About Us
class EmobotAbout(View):
	def get(self, request):
		return render(request, 'aboutus.html')

# Video
class EmobotVideo(View):
	def get(self, request):
		return render(request, 'facerecog.html')

# Text
class EmobotText(View):
	def get(self, request):
		return render(request, 'textrecog.html')

# Home
class EmobotHome(View):
	def get(self, request):
		return render(request, 'homepage.html')		


# Signup
def EmobotSignup(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		form2 = PersonForm(request.POST)
		if form.is_valid() and form2.is_valid():
			fn = request.POST.get('firstname')
			ln = request.POST.get('lastname')
			ha = request.POST.get('homeaddress')
			pr = request.POST.get('province')
			ct = request.POST.get('city')
			gn = request.POST.get('gender')
			bd = request.POST.get('birthday')

			form2 = Person(firstname = fn, lastname = ln, homeaddress = ha, 
						province = pr, city = ct, gender = gn, birthday = bd)

			form.save()
			form2.save()

			messages.success(request, 'Your account was created successfully' )
			return render(request, 'signup.html')
		
		else:
			return HttpResponse('not valid')

	context = {'form' : form}
	return render(request, 'signup.html', context)


# Login
def EmobotLogin(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return render(request, 'homepage.html')
		else:
			messages.info(request, 'Username or Password is Incorrect')
			return render(request, 'login.html')

	context = {}
	return render(request, 'login.html', context)


# Logout
def EmobotLogout(request):
	logout(request)
	return render(request, 'login.html')
