from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'home/home.html')

def forum(request):
    return render(request, 'home/forum.html')

def comments(request):
    return render(request, 'home/comments.html')

def aboutUs(request):
    return render(request, 'home/aboutUs.html')