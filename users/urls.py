from django.urls import path
from . import views

urlpatterns = [
    # path('pathName',views.functionName ,name='index')
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('signup/', views.signUpUser, name="signup"),


    path('profile/', views.profile, name="Profile"),]

