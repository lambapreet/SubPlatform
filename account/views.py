from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .forms import UserForm

# Create your views here.
def home(request):
    return render(request, 'account/index.html')


def register(request):
    form = UserForm()
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    context = {"form":form}
            
    return render(request, 'account/register.html', context)


def login(request):
    
    form =  AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username,password=password)
            
            if user is not None and user.is_writer == True:
                login(request, user)
                
                return redirect('home')
            
            if user is not None and user.is_writer == False:
                login(request, user)
                
                return redirect('home')
            
    context = {"LoginForm":form}        
    
        
    return render(request, 'account/login.html',context)
