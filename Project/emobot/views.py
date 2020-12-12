from django.http import HttpResponse
from django.http import Http404
from datetime import datetime
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from .forms import CreateUserForm
from .models import User, Person
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
		if form.is_valid():
			form.save()
			messages.success(request, 'Your account was created successfully' )
			return render(request, 'signup.html')

	context = {'form' : form}
	return render(request, 'signup.html', context)


# class EmobotSignup(View):
	# def get(self, request):
	# 	return render(request, 'signup.html')

	# def post(self, request):
	# 	form = UserForm(request.POST)

	# 	if form.is_valid():
	# 		fn = request.POST.get('firstname')
	# 		ln = request.POST.get('lastname')
	# 		ha = request.POST.get('homeaddress')
	# 		pr = request.POST.get('province')
	# 		ct = request.POST.get('city')
	# 		gn = request.POST.get('gender')
	# 		bd = request.POST.get('birthday')
	# 		em = request.POST.get('email')
	# 		un = request.POST.get('username')
	# 		pw = request.POST.get('password')
	
	# 		form = User(firstname = fn, lastname = ln, homeaddress = ha, 
	# 					province = pr, city = ct, gender = gn, birthday = bd, 
	# 					email = em, username = un, password = pw)

	# 		form.save() 

	# 		messages.success(request, 'Your account was created successfully!')

	# 		return render(request, 'signup.html')	

	# 	else:
	# 		print(form.errors)
	# 		return HttpResponse('not valid')

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
			messages.info(request, 'Username or Password in Incorrect')
			return render(request, 'login.html')

	context = {}
	return render(request, 'login.html', context)

# class EmobotLogin(View):
# 	def get(self, request):
# 		return render(request, 'login.html')

# 	def login(self, request):
# 		if request.method == 'POST':
# 			username = request.POST['username']
# 			password = request.POST['password']
			
# 			user = authenticate(request, username=username, password=password)

# 			if user is not None:
# 				login(request, user)
# 				return render(request, 'homepage.html')
# 			else:
# 				return HttpResponse('not valid')

# 		else:
# 			return HttpResponse('not valid')

def EmobotLogout(request):
	logout(request)
	return render(request, 'login.html')