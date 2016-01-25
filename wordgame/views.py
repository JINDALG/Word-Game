from django.shortcuts import render
from .models import Quiz,User
from django.http import HttpResponse,HttpResponseRedirect
from .forms	import Login_form,Register_form
from django import forms
import json,random

def login_check(request):
	try :
		user = User.objects.get(username = request.session['username'])
		return user
	except :
		return None
def index(request):
	user = login_check(request)
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

seq = None
count =None
def load_q(request):
	user  = login_check(request)
	if user :
		global seq
		global count
		if request.method =='POST' :
			# if count == 3 :
			# 	return render(request, 'wordgame/thanks.html', {'user' : user})
			if count == 0:
				seq = random.sample(range(1,4),3)
			q = Quiz.objects.get(pk=seq[count])
			response = {}
			options = random.sample(range(1,5),4)
			count +=1 
			i=1
			for option in options:
				response['option'+str(i)] = Quiz.objects.get(pk = option).meaning
				i += 1
			response['img'] = q.image_url
			response['question'] = q.question
			response['count'] = count
			response['score'] = user.score
			return HttpResponse(
				json.dumps(response),
				content_type='application/json'
			)
		else:
			return HttpResponseRedirect('/wordgame/game')
	else : 
		HttpResponseRedirect('/wordgame/game')

def check_ans(request):
	user = login_check(request)
	if user :
		if request.method == 'POST':
			try:
				q_text = request.POST.get('q_text')
				img = request.POST.get('img')
				u_answer = request.POST.get('u_answer')
				response = {}
				question = Quiz.objects.get(question= q_text, image_url = img)
				# return HttpResponse(q_text)
				if u_answer == question.meaning :
					user.score += 1
					user.save()
					response['complement'] = 'Good Job you are right!'
					response['answer'] = question.question + question.meaning
					response['sentence'] = question.sentence
					response['img'] = img
					response['main_word'] = question.main_word
					response['score'] = user.score
					return HttpResponse(
						json.dumps(response),
						content_type = 'application/json'
					)
				else :
					response['complement'] = 'Bad Guess, Better luck next time!'
					response['img'] = img
					response['score'] = user.score
					return HttpResponse(
						json.dumps(response),
						content_type = 'application/json'
					)
			except :
				return HttpResponseRedirect('/wordgame/game')
		else :
			return HttpResponseRedirect('/wordgame/game')		
	else :
		return HttpResponseRedirect('/wordgame/login')

def game(request):
	global seq
	global count
	seq = None
	count = 0
	user = login_check(request)
	if user :
		if request.method == 'post':
			return HttpResponse('Hello: ' + user.username + '\n' + 'Your score is : ' + user.score)
		else :
			user.score = 0
			user.save()
			return render(request , 'wordgame/game.html' , {'user' : user})
	else :
		return HttpResponseRedirect('/wordgame/login')