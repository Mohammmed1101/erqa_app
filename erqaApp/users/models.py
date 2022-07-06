from distutils.command.upload import upload
from email.policy import default
from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
# create schema

#class Employee(models.Model):
#    emp_no = models.IntegerField(('employee number'), primary_key=True)
#    birth_date = models.DateField(('birthday'))
#    first_name = models.CharField(('first name'), max_length=14)
#    last_name = models.CharField(('last name'), max_length=16)
#    gender = models.CharField(('gender'), max_length=1)
#    hire_date = models.DateField(('hire date'))

#    class Meta:
#        verbose_name = ('employee')
#        verbose_name_plural = ('employees')
#        db_table = 'employees'

#    def __str__(self):
#        return "{} {}".format(self.first_name, self.last_name)
#




#class User(models.Model):
#    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)
#    username = models.CharField(max_length=100)
#    password = models.CharField(max_length=50)
#    email = models.CharField(max_length=200)
#    first_name = models.CharField(max_length=100)
#    last_name = models.CharField(max_length=100)

#    def __str__(self):
#     return self.username

# username, password, check password are the main 3 fields in Sign Up page

# there is a problem with the email and username columns 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200,null=True, blank=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200,null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    location =  models.CharField(max_length=200,null=True, blank=True)
    profile_image = models.ImageField(
        null=True, blank=True, upload_to='images/', default="images/default-profilePicture.png" )
    join_date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                            primary_key=True,editable=False)

    ''' To be added later'''
    # uploaded_books =
    # user_comments =
    
    def __str__(self):
     return str(self.username)
