import django
from django import forms
from django.contrib.auth.forms import UserCreationForm
#####################
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.translation import ugettext
from rest_framework import fields, models, serializers, viewsets

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


MIN_LENGTH = 8


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

   queryset = User.objects.all()
   serializer_class = UserSerializer

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

