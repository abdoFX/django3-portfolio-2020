from django.shortcuts import render, get_object_or_404
from .models import blog

def all_blogs(request):
    blogs = blog.objects.order_by('-date')
    return render(request,"blog/all_blogs.html", {'blogs': blogs})

def detail(request,blog_id):
    blog_item = get_object_or_404(blog, pk=blog_id)
    return render(request,'blog/detail.html', {'blog':blog_item})