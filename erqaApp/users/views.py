from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def signup(request):
    return HttpResponse('Sign Up page')

# in terminal : python manage.py runserver
# http://127.0.0.1:8000/users/signup/