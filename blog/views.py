from django.shortcuts import render
from .models import Post

def blog_index(request):
    posts = Post.objects.all().order_by("-created_at")
    context = {'posts': posts}
    return render(request, 'blog/blog_index.html', context)

def blog_detail(request, id):
    post = Post.objects.get(pk=id)
    context = {'post': post}
    return render(request, 'blog/blog_detail.html', context)

def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by('-created_at')
    context = {'posts': posts, 'category': category}
    return render(request, 'blog/blog_category.html', context)
