from django import forms 
from .models import User
from django.contrib.auth.forms import UserCreationForm
class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']


class LoginForm(forms.Form):
    uname=forms.CharField(max_length=30)
    passw=forms.CharField(max_length=10)