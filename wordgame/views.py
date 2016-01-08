from django.shortcuts import render
from .models import Quiz,User
from django.http import HttpResponse,HttpResponseRedirect
from .forms	import Login_form,Register_form
from django import forms


def index(request):
	return HttpResponse('Hello.. Welcome to word-Game')


def login(request):
	if request.method == 'POST':
		if 'login' in request.POST:
			return HttpResponseRedirect('/wordgame')
		if 'register' in request.POST:
			form = Register_form(request.POST)
			if form.is_valid():
				username = form.cleaned_data['Username']
				password = form.cleaned_data['Password']
				repeat_password = form.cleaned_data['Repeat_Password']
				if len(username) < 3:
					Login_fields = Login_form()
					Register_fields  =Register_form()
					error = "Username must conatain at least 3 character"
					return render(request , 'wordgame/login.html' , {'Login_fields' : Login_fields, 'Register_fields' : Register_fields,'error' : error})
				if len(password) < 3:
					Login_fields = Login_form()
					Register_fields  =Register_form()
					error = "Password must conatain at least 3 character"
					return render(request , 'wordgame/login.html' , {'Login_fields' : Login_fields, 'Register_fields' : Register_fields,'error' : error})
				if password != repeat_password :
					Login_fields = Login_form()
					Register_fields  =Register_form()
					error = "Password does not match!"
					return render(request , 'wordgame/login.html' , {'Login_fields' : Login_fields, 'Register_fields' : Register_fields,'error' : error})
				try :
					user_already_exist  = User.object.get(user_name = username)
				except :
					print "something here"
			else :
				errors = form.errors
				error = errors.values()
				Login_fields = Login_form()
				Register_fields  =Register_form()
				error = error[0]
				return render(request , 'wordgame/login.html' , {'Login_fields' : Login_fields, 'Register_fields' : Register_fields,'error' : error})



	else :
		Login_fields = Login_form()
		Register_fields  =Register_form()
		return render(request , 'wordgame/login.html' , {'Login_fields' : Login_fields, 'Register_fields' : Register_fields})





