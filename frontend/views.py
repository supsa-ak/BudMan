from django.shortcuts import render, redirect
from django.http import JsonResponse
from .decorators import unauthenticated_user
from .forms import SignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

def home(request):
    context = {}
    return render(request, 'home.html',context)

@unauthenticated_user
def loginPage(request):
    form = SignupForm()
    if request.method == 'POST':
        if request.POST.get("form_type") == 'Login':
            username = request.POST.get('username')
            password = request.POST.get('password')
           
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

    context = {'form':form}
    return render (request, 'login.html', context)


@unauthenticated_user
def signupPage(request):
    form = SignupForm()
    if request.method == 'POST':
        if request.POST.get("form_type") == 'Sign up':
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created for '+ request.POST['username'])
                return redirect('login')
    context = {'form':form}
    return render (request, 'signup.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')