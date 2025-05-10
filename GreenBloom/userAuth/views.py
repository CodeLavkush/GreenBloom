from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return redirect('login/')

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form' : form})

def user_register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')

            user = User(username=username, email=email, password=password1)
            user.set_password(password1)
            user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {"form" : form})

def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect(settings.LOGOUT_REDIRECT_URL)