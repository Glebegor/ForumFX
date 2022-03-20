from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import register, comm, loginn

# Create your views here.
def base(request):
    return render(request, 'home/home.html')

def forum(request):
    return render(request, 'home/forum.html')
def aboutUs(request):
    return render(request, 'home/aboutUs.html')
    
def save_page(request):
   Name = request.POST["Name"]
   Email = request.POST["Email"]
   password = request.POST["password"]

def comments(request):
    if request.method == 'POST':
        form = comm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    else:
        form = comm()
    return render(request, 'home/comments.html', {'form': form})

def reg(request):
    if request.method == 'POST':
        form = register(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')    

    else:
        form = register()
    return render(request, 'home/reg.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = loginn(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')    

    else:
        form = loginn()
    return render(request, 'home/login.html', {'form': form})