from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as myLogin
from django.contrib.auth.decorators import login_required
from .decorators import *
from .models import *

# Create your views here.

from .forms import *





@notLoggedUser
def register(request):
    form = CreateNewUser()
    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, user + ' Created Successfully !')
            return redirect('login')

    context ={'form':form}
    return render(request, 'main/register.html', context)




@notLoggedUser
def userLogin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            myLogin(request, user)
            if request.user.is_staff:
                return redirect('home')
            
        else:
            messages.info(request, 'User Name or Password not Valid')

    context ={}
    return render(request, 'main/login.html', context)

@notLoggedUser
def userLogin_ar(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            myLogin(request, user)
            if request.user.is_staff:
                return redirect('home')
            
        else:
            messages.info(request, 'User Name or Password not Valid')

    context ={}
    return render(request, 'main/login_ar.html', context)


def userLogout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def No_Permission(request):
    context = {}
    return render(request, 'main/no_permission.html', context)

@login_required(login_url='login')
def home(request):
    user_profile = User_Profile.objects.get(user=request.user)

    user_permission = User_Permission.objects.get(user=request.user)


    context = {'user_profile':user_profile,

               'user_contract_permission':user_permission,

               }
    return render(request, 'main/home.html', context)



@login_required(login_url='login')
def user_profile(request):
    user_profile = User_Profile.objects.get(user=request.user)
    context = {'user_profile':user_profile}
    return render(request, 'main/user_profile.html', context)



