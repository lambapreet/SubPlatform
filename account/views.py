from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
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


def login_view(request):
    form = AuthenticationForm()
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None and user.is_writer is True:
                auth_login(request, user)
                return redirect('writer-dashboard')   # ✅ fixed typo
            
            if user is not None and user.is_writer is False:
                auth_login(request, user)
                return redirect('client-dashboard')
            
    context = {"LoginForm": form}        
    return render(request, 'account/login.html', context)


def logout_view(request):   # ✅ renamed to avoid clashing with django.contrib.auth.logout
    auth_logout(request)
    return redirect("login")
