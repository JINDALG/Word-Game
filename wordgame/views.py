from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Quiz,User
from django.http import HttpResponse,HttpResponseRedirect
from .forms	import Login_form,Register_form
from django import forms
import json,random
from django.views.generic import View

def login_check(request):
	try :
		user = User.objects.get(email = request.session['user'])
		return user
	except :
		return None

def index(request):
	user = login_check(request)
	return render(request , 'wordgame/index.html' , {'user' : user})

def Authenticate(email,Password):
	try :
		user = User.objects.get(email = email)
		if user.password == Password:
			return user
		return None
	except :
		return None
		
class LoginView(View):
	template = 'wordgame/login.html'
	Login_fields = Login_form
	Register_fields  =Register_form
	def login(self,request,email):
		request.session['user'] = email
	def get(self,request):
		if login_check(request) :
			return HttpResponseRedirect('/')
		return render(request , self.template , {'Login_fields' : self.Login_fields(), 'Register_fields' : self.Register_fields()})
	def post(self,request):
		if 'login' in request.POST:
			form = self.Login_fields(request.POST)
			if form.is_valid():
				email = request.POST.get('email')
				password = request.POST.get('password')
				user = Authenticate(email,password)
				if user:
					self.login(request,email)
					return HttpResponseRedirect('/')
				else:
					print email
					print password
					error = "username and password does not match"
					return render(request , self.template , {
						'Login_fields' : form, 
						'Register_fields' : self.Register_fields(),
						'error' : error,
						'method':'login'})
			else :
				error = form.errors
				return render(request , self.template , {
					'Login_fields' : form, 
					'Register_fields' : self.Register_fields(),
					'errors' : error.values(),
					'method':'login'})
		elif 'register' in request.POST:
			form = self.Register_fields(request.POST)
			if form.is_valid():
				username = request.POST.get('username')
				username = username.capitalize()
				email = request.POST.get('email')
				password = request.POST.get('password')
				c_password = request.POST.get('c_password')
				if password == c_password:
					user = User(username = username, email = email, password = password)
					user.save()
					request.session['user'] = str(email)
					return HttpResponseRedirect('/')
				else :
					error = "password does not match"
					return render(request, self.template, {
						'Login_fields' : self.Login_fields(), 
						'Register_fields' : form,
						'error':errors,
						'method':'register'})
			else :
				error = form.errors
				return render(request, self.template, {
					'Login_fields' : self.Login_fields(), 
					'Register_fields' : form,
					'errors' : error,
					'method':'register'})
def logout(request):
	try:
		del request.session['user']
	except:
		return HttpResponseRedirect('/')
	return HttpResponseRedirect('/')

seq = None
count =None
@csrf_exempt
def load_q(request):
	user  = login_check(request)
	if user :
		global seq
		global count
		if request.method =='POST' :
			# if count == 3 :
			# 	return render(request, 'wordgame/thanks.html', {'user' : user})
			if count == 0:
				seq = random.sample(range(1,5),4)
			try :
				q = Quiz.objects.get(pk=seq[count])
				response = {}
				options = random.sample(range(1,5),4)
				i=1
				for option in options:
					response['option'+str(i)] = Quiz.objects.get(pk = option).meaning
					i += 1
				response['img'] = str(q.image_url.url)
				response['question'] = q.question
				response['count'] = count
				response['score'] = user.score
				return HttpResponse(
					json.dumps(response),
					content_type='application/json'
				)
			except :
				return HttpResponse(
					json.dumps(dict(error = 'error')),
					content_type='application/json'
				)
		else:
			return HttpResponseRedirect('/game')
	else : 
		HttpResponseRedirect('/game')

@csrf_exempt
def check_ans(request):
	user = login_check(request)
	if user :
		global seq
		global count
		if request.method == 'POST':
			try:
				# q_text = request.POST.get('q_text')
				# img = request.POST.get('img')
				u_answer = request.POST.get('u_answer')
				question = Quiz.objects.get(pk=seq[count])
				count += 1
				response = dict(u_answer = u_answer)
				response['img'] = str(question.image_url.url)
				if u_answer == question.meaning :
					user.score += 1
					user.save()
					response['complement'] = 'Good Job you are right!'
					response['question'] = "Given Word: " +  question.question
					response['answer'] = "Meaning: " + question.meaning
					response['sentence'] =  "Sentence: " + question.sentence
					response['main_word'] = "Main Word: " + question.main_word
					response['score'] = user.score
					return HttpResponse(
						json.dumps(response),
						content_type = 'application/json'
					)
				elif u_answer == "None":
					response['complement'] = 'Time out, try next question'
				else :
					response['complement'] = 'Bad Guess, Better luck next time!'

				response['score'] = user.score
				return HttpResponse(
					json.dumps(response),
					content_type = 'application/json'
				)

			except :
				return HttpResponseRedirect('/game')
		else :
			return HttpResponseRedirect('/game')		
	else :
		return HttpResponseRedirect('/login')
@csrf_exempt
def game(request):
	global seq
	global count
	count = 0
	user = login_check(request)
	if user :
		if request.method == 'POST':
			return render(request, 'wordgame/thanks.html', {'user' : user})
		else :
			user.score = 0
			user.save()
			return render(request, 'wordgame/game.html' , {'user' : user})
	else :
		return HttpResponseRedirect('/login')