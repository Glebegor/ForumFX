from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import register

# Create your views here.
def base(request):
    return render(request, 'home/home.html')

def forum(request):
    return render(request, 'home/forum.html')

def comments(request):
    return render(request, 'home/comments.html')

def aboutUs(request):
    return render(request, 'home/aboutUs.html')
    
def save_page(request):
   Name = request.POST["Name"]
   Email = request.POST["Email"]
   password = request.POST["password"]


def reg(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = register(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = register()
    return render(request, 'home/reg.html', {'form': form})