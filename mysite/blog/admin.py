from django.contrib import admin
from .models import BlogPost, Comment, Visitors

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Comment)

