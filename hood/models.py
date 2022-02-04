from time import time
from unicodedata import category
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# class Service(models.Model):
#     category =  models.TextField()  
#     phone_number = models.CharField(max_length=12) 
#     rate = models.IntegerField()

class Business(models.Model):
    name =models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField()
    address =models.CharField(max_length=100)
    contact = models.IntegerField()

    def __str__(self):
        return self.name

class Authority(models.Model):
    name =models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField()
    address =models.CharField(max_length=100)
    contact = models.IntegerField()

    def __str__(self):
        return self.name        


class HealthService(models.Model):
    name =models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField()
    address =models.CharField(max_length=100)
    contact = models.IntegerField()

    def __str__(self):
        return self.name        