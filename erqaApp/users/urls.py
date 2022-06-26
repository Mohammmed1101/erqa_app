from django.urls import path
from . import views
from views import signup

urlpatterns = [
    # path('pathName',views.functionName ,name='index')
    path('signup/' , views.signup , name = 'Sign Up')
]