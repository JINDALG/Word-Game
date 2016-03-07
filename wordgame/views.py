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

class profile(View):
	template = 'wordgame/profile.html'
	def get(self,request,user_name):
		try :
			puser = User.objects.get(username = user_name.capitalize())
			user = login_check(request)
			return render(request, self.template, {'puser' : puser,'user' : user})
		except:
			return HttpResponseRedirect('/')
		
class LoginView(View):
	template = 'wordgame/login.html'
	Login_fields = Login_form
	Register_fields  =Register_form
	def login(self,request,email):
		request.session['user'] = email
	def get(self,request):
		if login_check(request) :
			return HttpResponseRedirect('/')
		return render(request , self.template, {})
	def post(self,request):
		error  = None
		if 'login' in request.POST:
			form = self.Login_fields(request.POST)
			if form.is_valid():
				email = request.POST.get('email')
				password = request.POST.get('password')
				user = Authenticate(email,password)
				if user:
					self.login(request,email)
					return HttpResponseRedirect('/')
				error = "username and password does not match"
			errors = form.errors
			return render(request , self.template , {
				'Login' : form,
				'Login_error' : error, 
				'Login_errors' : errors.values()})

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
				error = "Password does not match"
	
			errors = form.errors
			return render(request, self.template, {
				'Register' : form,
				'register_error' : error,
				'register_errors' : errors})
def logout(request):
	try:
		del request.session['user']
		del request.session['score'] 
		del request.session['count']
		del request.session['seq']
	except:
		return HttpResponseRedirect('/')
	return HttpResponseRedirect('/')
 
slot_size = None
@csrf_exempt
def load_q(request):
	global slot_size
	user  = login_check(request)
	if user :
		if request.method =='POST' :
			response = {}
			if request.session['count'] == 0:
				slot_size = 3
				request.session['seq'] = random.sample(range(1,len(Quiz.objects.all())+1),slot_size)
			try :
				seqe = request.session['seq']
				q = Quiz.objects.get(pk=seqe[request.session['count']])
				options = random.sample(range(1,len(Quiz.objects.all())+1),4)
				print options
				if q.id not in options:
					options[2] = q.id
				
				random.shuffle(options)
				print options
				i=1
				for option in options:
					response['option'+str(i)] = Quiz.objects.get(pk = option).meaning
					i += 1
				response['img'] = str(q.image_url.url)
				response['word'] = q.word.capitalize()
				print response
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
	global slot_size
	user = login_check(request)
	if user :
		if request.method == 'POST':
			try:
				u_answer = request.POST.get('u_answer')
				sequ = request.session['seq']
				question = Quiz.objects.get(pk=sequ[request.session['count']])
				response = dict(u_answer = u_answer,count = request.session['count']+1)
				request.session['count'] +=1
				response['img'] = str(question.image_url.url)
				response['slot_size'] = slot_size
				response['word'] = "Word: " + question.word.capitalize()
				if u_answer == question.meaning :
					request.session['score'] +=1
					response['complement'] = 'Good Job you are right!'
					response['phrase'] = "Phrase: " +  question.phrase
					response['meaning'] = "Meaning: " + question.meaning
					response['sentence'] =  "Sentence: " + question.sentence
					return HttpResponse(
						json.dumps(response),
						content_type = 'application/json'
					)
				elif u_answer == "None":
					response['complement'] = 'Time out, try next question'
				else :
					response['complement'] = 'Bad Guess, Better luck next time!'
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
	user = login_check(request)
	if user :
		if request.method == 'POST':
			if request.session.get('count',None) == None:
				score = map(int,user.score.split(','))
				score = score[-1]
			else :
				if user.score == "":
					user.score = request.session['score']
				else:
					user.score += ',' + str(request.session['score'])
				user.save()
				score = request.session['score']
				del request.session['count']
				del request.session['seq']
				del request.session['score']
			per = round(score/15.0,2)
			
			return render(request, 'wordgame/thanks.html', {'user' : user,'score' : score,'percent':per})
		else :
			if request.session.get('count',None) == None:
				request.session['score'] = 0
				request.session['count'] = 0	
			return render(request, 'wordgame/game.html' , {'user' : user})
	else :
		return HttpResponseRedirect('/login')