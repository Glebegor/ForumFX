from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import commentsTabl
from django.contrib.auth.models import User

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
def login(request):
    return render(request, 'home/login.html')