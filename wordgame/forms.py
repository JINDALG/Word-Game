from django import forms
from .models import User

class Login_form(forms.Form):
	email = forms.EmailField()
	password = forms.CharField()

class Register_form(forms.ModelForm):
	c_password = forms.CharField()
	class Meta:
		model = User
		fields = ['username','email', 'password', 'c_password']

