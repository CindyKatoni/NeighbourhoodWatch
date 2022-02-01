from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='hood-login'),
    path('home/', views.home, name='hood-home'),
   
]