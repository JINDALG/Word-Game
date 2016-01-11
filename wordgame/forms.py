from django import forms

class Login_form(forms.Form):
	Username = forms.CharField(label='Username' , max_length = 20);
	Password = forms.CharField(widget = forms.PasswordInput, label='Password' , max_length = 20);


class Register_form(forms.Form):
	Username = forms.CharField(label = 'Username' , max_length=20);
	Password = forms.CharField(label='Password' , widget = forms.PasswordInput, max_length=20);
	Repeat_Password = forms.CharField(label = 'Repeat Password', widget = forms.PasswordInput , max_length=20);	
