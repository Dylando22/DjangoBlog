from datetime import datetime

from django.db import models

# Create your models here.
from django.http import request
from django.utils import timezone


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField(default="")
    posted = models.DateTimeField('date published')
    comment_count = models.IntegerField(default= 0)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.posted >= timezone.now() - datetime.timedelta(days=1)


class Comment(models.Model):
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    commenter = models.CharField(max_length=200)
    content = models.TextField(default="")
    email = models.EmailField(max_length=254)
    posted = models.DateTimeField('date published')

    def __str__(self):
        return self.commenter

    def was_published_recently(self):
        return self.posted >= timezone.now() - datetime.timedelta(days=1)


class Visitors(models.Model):
    who = models.CharField(max_length=127)
    when = models.DateTimeField('date published')

