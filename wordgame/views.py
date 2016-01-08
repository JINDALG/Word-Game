from django.shortcuts import render
from .models import Quiz,User
from django.http import HttpResponse,HttpResponseRedirect
from .forms	import Login_form,Register_form

def index(request):
	return HttpResponse('Hello.. Welcome to word-Game')


def login(request):
	if request.method == 'POST':
		if 'login' in request.POST:
			return HttpResponseRedirect('/wordgame')
		if 'register' in request.POST:
			Login_fields = Login_form()
			Register_fields  =Register_form()
			return render(request , 'wordgame/login.html' , {'Login_fields' : Login_fields, 'Register_fields' : Register_fields})

	else :
		Login_fields = Login_form()
		Register_fields  =Register_form()

	return render(request , 'wordgame/login.html' , {'Login_fields' : Login_fields, 'Register_fields' : Register_fields})





