from django.http import HttpResponse
from django.http import Http404
from datetime import datetime
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from .forms import UserForm
from .models import User, Person

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
class EmobotSignup(View):
	def get(self, request):
		return render(request, 'signup.html')

	def post(self, request):
		form = UserForm(request.POST)

		if form.is_valid():
			fn = request.POST.get('ufirstname')
			ln = request.POST.get('ulastname')
			ha = request.POST.get('uhomeaddress')
			pr = request.POST.get('uprovince')
			ct = request.POST.get('ucity')
			gn = request.POST.get('ugender')
			bd = request.POST.get('ubirthdate')
			em = request.POST.get('uemail')
			un = request.POST.get('uusername')
			pw = request.POST.get('upassword')

			form = User( firstname = fn, lastname = ln, homeaddress = ha, province = pr, 
									city = ct, gender = gn, birthday = bd, uemail = em,
									username = un, password = pw)

			form.save() 

			return render(request, 'login.html')		

		else:
			print(form.errors)
			return HttpResponse('not valid')

# Login
class EmobotLogin(View):
	def get(self, request):
		return render(request, 'login.html')		