from django.shortcuts import render
from .models import Quiz,User
from django.http import HttpResponse,HttpResponseRedirect
from .forms	import Login_form,Register_form
from django import forms
import json


def index(request):
	user = None
	try :
		user = request.session['username']
		user = User.objects.filter(username = user)
		user = user[0]
	except :
		return render(request , 'wordgame/base.html' , {'user' : user})
	return render(request , 'wordgame/base.html' , {'user' : user})

def login(request):
	if request.method == 'POST':
		Login_fields = Login_form()
		Register_fields  =Register_form()
		if 'login' in request.POST:
			form = Login_form(request.POST)
			if form.is_valid():
				username = form.cleaned_data['Username']
				password = form.cleaned_data['Password']
				user = User.objects.filter(username = username)
				if user and user[0].password == password:
					request.session['username'] = username
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
		del request.session['username']
	except:
		return HttpResponseRedirect('/wordgame')
	return HttpResponseRedirect('/wordgame')

q = None

def load_q(request):
	global q
	if request.method =='DELETE' : 
		q = Quiz.objects.all()
		q1 = q[0]
		response = {}
		response['img'] = q1.image_url
		response['question'] = q1.question
		return HttpResponse(
			json.dumps(response),
			content_type='application/json'
		)
	else:
		return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def game(request):
	user = None
	try :
		user = request.session['username']
		user = User.objects.filter(username = user)
		user = user[0]
		if request.method == 'POST':
			return HttpResponse('Hello: ' + user.username + '\n' + 'Your score is : ' + user.score)
		else :
			q = Quiz.objects.all()
			return render(request , 'wordgame/game.html' , {'user' : user})
	except :
		return HttpResponseRedirect('/wordgame/game')