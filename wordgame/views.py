from django.shortcuts import render
from .models import Quiz,User
from django.http import HttpResponse,HttpResponseRedirect
from .forms	import Login_form,Register_form
from django import forms




def index(request):
	try :
		user = request.session['user']
		user = User.objects.filter(username = user)
		return HttpResponse('Hello.. %s' %user[0].username)
	except :
		return HttpResponse('you are not logged in')


def login(request):
	if request.method == 'POST':
		if 'login' in request.POST:
			form = Login_form(request.POST)
			if form.is_valid():
				username = form.cleaned_data['Username']
				password = form.cleaned_data['Password']
				user = User.objects.filter(username = username)
				if user and user[0].password == password:
					request.session['user'] = username
					return HttpResponseRedirect('/wordgame')
				else :
					error = "username and password does not match"
					return render(request , 'wordgame/login.html' , {'Login_fields' : Login_fields, 'Register_fields' : Register_fields,'error' : error})
			return HttpResponseRedirect('/wordgame')
		if 'register' in request.POST:
			form = Register_form(request.POST)
			if form.is_valid():
				username = form.cleaned_data['Username']
				password = form.cleaned_data['Password']
				repeat_password = form.cleaned_data['Repeat_Password']
				Login_fields = Login_form()
				Register_fields  =Register_form()
				if len(username) < 3:
					error = "Username must conatain at least 3 character"
					return render(request , 'wordgame/login.html' , {'Login_fields' : Login_fields, 'Register_fields' : Register_fields,'error' : error})
				if len(password) < 3:
					error = "Password must conatain at least 3 character"
					return render(request , 'wordgame/login.html' , {'Login_fields' : Login_fields, 'Register_fields' : Register_fields,'error' : error})
				if password != repeat_password :
					error = "Password does not match!"
					return render(request , 'wordgame/login.html' , {'Login_fields' : Login_fields, 'Register_fields' : Register_fields,'error' : error})

				user = User.objects.filter(username = username)
				if user:
					error  ="user already exist"
					return render(request , 'wordgame/login.html' , {'Login_fields' : Login_fields, 'Register_fields' : Register_fields,'error' : error})
				else :
					user = User(username = username, password=password)
					user.save()
					return HttpResponseRedirect('/wordgame')
					
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


def logout(request):
	try:
		del request.session['user']
	except KeyError:
		return HttpResponseRedirect('/wordgame')
	return HttpResponseRedirect('/wordgame')