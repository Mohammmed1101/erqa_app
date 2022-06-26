from django.db import models

# Create your models here.
# create schema

class Employee(models.Model):
    emp_no = models.IntegerField(('employee number'), primary_key=True)
    birth_date = models.DateField(('birthday'))
    first_name = models.CharField(('first name'), max_length=14)
    last_name = models.CharField(('last name'), max_length=16)
    gender = models.CharField(('gender'), max_length=1)
    hire_date = models.DateField(('hire date'))

    class Meta:
        verbose_name = ('employee')
        verbose_name_plural = ('employees')
        db_table = 'employees'

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
#
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)