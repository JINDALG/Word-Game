from django.shortcuts import render
from .models import Quiz,User
from django.shortcuts import render
from django.http import HttpResponse

def index(request,user_name):
	if request.method == 'POST':

	else :
		render(request,wordgame/index.html)


