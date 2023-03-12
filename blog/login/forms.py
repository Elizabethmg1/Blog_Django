from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegisterForm(UserCreationForm):
    username= forms.CharField(max_length=50)
    email= forms.EmailField()
    password1 = forms.CharField(label='password1',widget=forms.PasswordInput)
    password2 = forms.CharField(label='password2',widget=forms.PasswordInput)

    class Meta:
        model =  User
        fields = ['username', 'email', 'password1', 'password2']