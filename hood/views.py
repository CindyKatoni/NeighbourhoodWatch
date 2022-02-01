from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def login(request):
    return render(request, 'hood/login.html')

def home(request):
    return render(request, 'hood/home.html', {'title': 'Watch'})

 