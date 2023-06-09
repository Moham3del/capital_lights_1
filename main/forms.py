from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *



class CreateNewUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class Profile_Form(ModelForm):
    class Meta:
        model = User_Profile
        fields = "__all__"


