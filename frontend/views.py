from django.shortcuts import render
from django.http import JsonResponse
from .decorators import unauthenticated_user
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'frontend/home.html')

@unauthenticated_user
def loginPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        if request.POST.get("form_type") == 'Sign up':
            if request.method == 'POST' :
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    user = form.save()
                    user.save()
                    messages.success(request, 'Account created for '+ user.username)
                    return redirect('login')
                    

        elif request.POST.get("form_type") == 'Login':
            username = request.POST.get('username')
            password = request.POST.get('password')
           
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

    context = {'form':form}
    return render (request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')