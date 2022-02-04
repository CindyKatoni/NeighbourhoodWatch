from django.contrib import admin
from .models import Post, Business, Authority, HealthService
# Register your models here.
admin.site.register(Post)
admin.site.register(Business)
admin.site.register(Authority)
admin.site.register(HealthService)