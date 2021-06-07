from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'base.html')

def login(request):
    return render(request, 'login.html')

def signUp(request):
    return render(request,'signUp.html')

def feed(request):
    return render(request,'feed.html')

def profile(request):
    return render(request,'profile.html')