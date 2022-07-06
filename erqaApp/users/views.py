from email import message
from urllib import request
from urllib.request import Request
import django
from django import forms
from .forms import SignupForm
#####################
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
#from django.utils.translation import ugettext
#from rest_framework import fields, serializers, viewsets
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
# class UserSeriaalizer(serializers.ModelSerializer):
#     pass
# def signup(request):
#     return HttpResponse('Sign Up page')

 # in terminal : python manage.py runserver
 # http://127.0.0.1:8000/users/signup/

# #Sign up

# def signup (request):
#     form = UserCreationForm(request.post or None, request.FILES or None)
#     if form.is_valid():
#         form.save()
#         return redirect('list_all_departments')

#     return render(request, 'erqaApp/SignUp.html', {'form':form})


# #Validate whether the password is alphanumeric

# class NumericPasswordValidator:
    
#     def validate(self, password, user=None):
#         if password.isdigit():
#             raise ValidationError(
#                 _("This password is entirely numeric."),
#                 code='password_entirely_numeric',
#             )

#     def get_help_text(self):
#         return _("Your password should be alphanumeric.")


# we should add decorators above each view that requires sign in 
# such as adding books and so on

'''MIN_LENGTH = 8

class UserSerializer(serializers.ModelSerializer):

   password = serializers.CharField(
     write_only=True,
     min_length=MIN_LENGTH,
     error_messages={
       "min_length": f"Password must be longer than {MIN_LENGTH} characters."
     }
   )
   password2 = serializers.CharField(
     write_only=True,
     min_length=MIN_LENGTH,
     error_messages={
       "min_length": f"Password must be longer than {MIN_LENGTH} characters."
     }
   )
  
   class Meta:
     model = User
     fields = "__all__"

   def validate(self, data):
     if data["password"] != data["password2"]:
       raise serializers.ValidationError("Password does not match.")
     return data
  
   def create(self, validated_data):
     user = User.objects.create(
       username=validated_data["username"],
       email=validated_data["email"],
       first_name=validated_data["first_name"],
       last_name=validated_data["last_name"],
     )

     user.set_password(validated_data["password"])
     user.save()

     return user   

class UserViewSet(viewsets.ModelViewSet):

   queryset = User.objects.all()'''
   #serializer_class = UserSerializer

######################################

# def validate(min_length, password):
#     special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
#     if len(password) < 8:
#         raise ValidationError(ugettext('Password must be at least 8 character.'))
#     if not any(char.isdigit() for char in password):
#         raise ValidationError(ugettext('Password must contain at least %(min_length)d digit.') % {'min_length': min_length})
#     if not any(char.isalpha() for char in password):
#         raise ValidationError(ugettext('Password must contain at least %(min_length)d letter.') % {'min_length': min_length})
#     if not any(char in special_characters for char in password):
#         raise ValidationError(ugettext('Password must contain at least %(min_length)d special character.') % {'min_length': min_length})


def signup(request):
  return render(request, 'users/signup.html')

def loginUser(request):
  # to send the user to the main page after logging in
  page = 'login'

  if request.user.is_authenticated:
    return redirect('Profile')


  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    try:
      user = User.objects.get(username=username)
    except:
      messages.error(request, ' Username does not exist ')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('Profile')
    else:
      messages.error(request,' Username or password in not correct ')

  return render(request, 'users/login_register.html')



def logoutUser(request):
  logout(request)
  messages.error(request, ' User logged out successfully ')

  return redirect('login')



def signUpUser(request):
  page = 'signup'

  #We are using Django built in registration forms
  form = SignupForm()

  if request.method == 'POST':
    form = SignupForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.username = user.username.lower()
      user.save()

  #Success flash message 
      messages.success(request, ' Account successfully created ! ')

  #redirecting the user to profiles page after sign up
      login(request, user)
      return redirect('Profile')
    else:   #Error flash message 
      messages.error(request, ' An error accurred while signing up! ')

  context = {'page' : page, 'form': form}
  return render(request, 'users/login_register.html', context)



def profile(request):
  users = User.objects.all()
  profiles = Profile.objects.all()
  context = {'profiles' : profiles , 'users': users } #in the '' is the name usen in Jinja
  return render(request, 'users/profile.html', context)