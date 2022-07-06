from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

#Creating Signup Form with three fields
class SignupForm( UserCreationForm ):

    first_name= forms.CharField(max_length=200)
    last_name=forms.CharField(max_length= 200)
    email = forms.EmailField(label= 'Your Email', max_length= 254, help_text='example@email.com')
    username = forms.CharField(max_length= 200)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']


