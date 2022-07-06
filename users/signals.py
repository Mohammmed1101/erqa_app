from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver



def createProfile(sender, instance, created, **lwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user= user,
            name= user.first_name,
            username = user.username,
            email = user.email,
        )

def deleteUser (sender, instance, **lwargs):
    user = instance.user
    user.delete()
    print('Deleting user ... ')

post_save.connect(createProfile, sender=User)

post_delete.connect(deleteUser, sender=Profile)