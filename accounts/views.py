from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['Username'], cd['Email'], cd['Password'])
            messages.success(request,'registered', 'success')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['Username'], password=cd['Password'])
            if user is not None:
                login(request, user)
                messages.success(request,'login', 'success')
                return redirect('home')
            else:
                messages.error(request, 'username or password is wrong', 'danger')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form':form})
def user_logout(request):
    logout(request)
    messages.success(request, 'loging out', 'success')
    return redirect('home')