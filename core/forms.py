from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 



class userForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email-address'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter confirm-password'}))
    
    
    class Meta:
        model = User 
        fields  = ['username', 'email', 'password1', 'password2']
