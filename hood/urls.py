from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingpage, name='hood-landingpage'),
    path('home/', views.home, name='hood-home'),
    path('blog/', views.blog, name='hood-blog'),
   
]