from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView    
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from .forms import CommentForm
from .models import Comment
from django.utils import timezone

# Create your views here.
def base(request):
    return render(request, 'home/home.html')
def forum(request):
    return render(request, 'home/forum.html')
def aboutUs(request):
    return render(request, 'home/aboutUs.html')

def comments(request):
    comments = Comment.objects.all()
    form = CommentForm()
    context = {"comments": comments, "form": form}
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.avtor = request.user
            comment.save() 
            return HttpResponseRedirect(reverse('comment'))
        else:
            context["form"] = form
            return render(request, "home/comments.html", context)
    else:
        return render(request, "home/comments.html", context)
