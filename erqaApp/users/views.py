import django
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import viewsets , serializers

# Create your views here.
class UserSeriaalizer(serializers.ModelSerializer):
    pass
def signup(request):
    return HttpResponse('Sign Up page')

# in terminal : python manage.py runserver
# http://127.0.0.1:8000/users/signup/
