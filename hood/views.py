from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def login(request):
    return HttpResponse('<h1> hood login </h1>')

def home(request):
    return HttpResponse('<h1> hood home </h1>')

 