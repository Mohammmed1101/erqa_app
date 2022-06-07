from django.urls import path
from . import views

urlpatterns = [
    # path('pathName',views.functionName ,name='index')
    path('signup/' , views.signup , name = 'signup')
]