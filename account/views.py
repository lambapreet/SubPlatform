from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login   # fix: avoid conflict with view
from .forms import UserForm


def home(request):
    return render(request, 'account/index.html')


def register(request):
    form = UserForm()
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    context = {"form": form}
    return render(request, 'account/register.html', context)


def login_view(request):   # fix: renamed to avoid clash
    form = AuthenticationForm()
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None and user.is_writer is True:
                auth_login(request, user)   # fix: call Django's login
                return redirect('writer-dashbaord')
            
            if user is not None and user.is_writer is False:
                auth_login(request, user)   # fix: call Django's login
                return redirect('client-dashboard')
            
    context = {"LoginForm": form}        
    return render(request, 'account/login.html', context)
