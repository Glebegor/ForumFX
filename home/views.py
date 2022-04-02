from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import commentsTabl
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView    
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

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
#     return render(request, 'home/login.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect(reverse('home'))
        else:
            messages.error(request,'username or password not correct')
            return redirect(reverse('home'))
        
                
    else:
        form = AuthenticationForm()
    return render(request,'home/login.html',{'form':form})