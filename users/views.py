from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages


def register(request):
    if request.method =="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(
        request, 
        'users/reg.html',
        {'form':form}
    )
