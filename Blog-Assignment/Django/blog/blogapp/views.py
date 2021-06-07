from typing import NewType
from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Blog
# from Django.blog.blogapp.views import create
# Create your views here.

def detail(request,id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request,'detail.html',{'blog': blog})

def home(request):
    blogs = Blog.objects.all()
    return render(request,'home.html',{'blogs':blogs})

def new(request):
    return render(request,'new.html')

def create(requset):
    new_blog = Blog()
    new_blog.title = requset.POST['title']
    new_blog.writer = requset.POST['writer']
    new_blog.body = requset.POST['body']
    new_blog.pub_date = timezone.now()
    new_blog.save()
    return redirect('detail', new_blog.id)

def edit(request,id):
    blog = Blog.objects.get(id = id)

    if request.method == "POST":
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect('detail', blog.id)

    else:
        return render(request, 'edit.html',{'blog':blog})