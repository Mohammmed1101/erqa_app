
from email.policy import default
from django import forms

#Creating Signup Form with three fields

class SignupForm(forms.Form):
    first_name=forms.CharField(max_length= 200)
    last_name=forms.CharField(max_length= 200)
    email = forms.EmailField(label= 'Your email', max_length= 254, help_text='example@email.com')
