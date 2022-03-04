import time

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import BlogPost, Comment, Visitors
from datetime import datetime

# Create your views here.
def index(request):
    recent_posts = BlogPost.objects.order_by('-posted')[:5]
    comments = Comment.objects.order_by('-id')
    data = Visitors(who=request.META['REMOTE_ADDR'],when=timezone.now())
    context = {'recent_posts': recent_posts[0:3],
               'comments': comments,
               'now': time.strftime('%c'),
               'visitor': data
               }
    return render(request, 'blog/index.html', context)

def blogpost(request, blog_id):
    post = get_object_or_404(BlogPost, pk=blog_id)
    comments = Comment.objects.order_by('-id')
    context = {
        'now': time.strftime('%c'),
        'comments': comments,
        'post': post
    }
    return render(request, 'blog/entry.html', context)

def archive(request):
    recent_posts = BlogPost.objects.order_by('-posted')[:5]
    comments = Comment.objects.all()
    data = Visitors(who=request.META['REMOTE_ADDR'],when=timezone.now())
    context = {'recent_posts': recent_posts,
               'now': time.strftime('%c'),
               'comments': comments,
               'visitor': data
               }
    return render(request, 'blog/archive.html', context)

def comment(request, blog_id):
    blog = get_object_or_404(BlogPost, pk=blog_id)
    if request.method == 'POST':
        comment = Comment()
        comment.blog = blog
        comment.commenter = request.POST.get('name')
        comment.content = request.POST.get('message')
        comment.email = request.POST.get('email')
        comment.posted = timezone.now()
        comment.save()

        blog.comment_count += 1
        blog.save()

        return HttpResponseRedirect(reverse('blog:blogpost', args=(blog_id,)))
    else:
        return render(request,'blog/index.html')




def plan(request):
    data = Visitors(who= request.META['REMOTE_ADDR'] ,when=timezone.now())
    context = {
        'visitor' : data,
        'now' : time.strftime('%c')
    }
    return render(request, 'blog/plan.html',context)

def about(request):
    data = Visitors(who=request.META['REMOTE_ADDR'],when=timezone.now())
    context = {
        'now' : time.strftime('%c'),
        'visitor' : data
    }
    return render(request, 'blog/about.html', context)

def ttpcss(request):
    context = {
        'now' : time.strftime('%c')
    }
    return render(request, 'blog/techtips+css.html',context)

def ttmcss(request):
    context = {
        'now' : time.strftime('%c')
    }
    return render(request, 'blog/techtips-css.html',context)


