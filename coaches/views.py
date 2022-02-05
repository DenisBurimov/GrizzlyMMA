from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    data = {
        'page_title' : 'Home Page',
        'posts' : Post.objects.all(),
    }

    return render(request, 'coaches/home.html', data)

def about(request):
    data = {
        'page_title' : 'About Page',
    }

    return render(request, 'coaches/about.html', data)

def groups(request):
    data = {
        'page_title' : 'Grizzly MMA Groups',
        'testing_content' : "Groups Page Testing Content",
    }

    return render(request, 'coaches/groups.html', data)

def coaches(request):
    data = {
        'page_title' : 'Тренерская',
        'testing_content' : "Тренерская",
    }

    return render(request, 'coaches/coaches.html', data)

def post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    data = {
        'page_title' : 'Home Page',
        'post' : post,
    }

    return render(request, 'coaches/article.html', data)
