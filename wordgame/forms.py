from django import forms

class Login_form(forms.Form):
	Username = forms.CharField(label='Username');
	Password = forms.CharField(widget = forms.PasswordInput(), label='Password');


class Register_form(forms.Form):
	Username = forms.CharField(label = 'Username');
	Password = forms.CharField(label='Password' , widget = forms.PasswordInput());
	Repeat_Password = forms.CharField(label = 'Repeat Password', widget = forms.PasswordInput());	
