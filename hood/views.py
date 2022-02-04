from django.shortcuts import render
from .models import Post, Business, Authority, HealthService
# Create your views here.

def landingpage(request):
    return render(request, 'hood/landingpage.html')


def home(request):
    return render(request, 'hood/home.html', {'title': 'Watch'})

def blog(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'hood/blog.html', context) 