from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import commentsTabl
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView    
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
# Create your views here.
def base(request):
    return render(request, 'home/home.html')
def forum(request):
    return render(request, 'home/forum.html')
def aboutUs(request):
    return render(request, 'home/aboutUs.html')
def comments(request):
    data = {
        'com': commentsTabl.objects.all()
    }
    if request.method =="POST":
        form = commentsTabl(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = commentsTabl()

    return render(request, 'home/comments.html', data,{'form':form})

# def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                auth_login(request,user)
                return redirect(reverse('home'))
            else:
                messages.error(request,'username or password not correct')
                return redirect(reverse('home'))
                
        else:
            form = AuthenticationForm()
    return render(request,'home/login.html',{'form':form})
# def login(request):
    msg = []
    if request.method == 'POST':
        username = request.POST['u']
        password = request.POST['p']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                msg.append("login successful")
            else:
                msg.append("disabled account")
        else:
            msg.append("invalid login")
    return render_to_response('login.html', {'errors': msg})
# def login(request):
    if request.user.is_authenticated:
        return render(request, 'home/login.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'home/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'home/login.html', {'form': form})