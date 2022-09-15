from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author': 'CoreyMs',
        'title': 'Blog Post',
        'content': 'First',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Subhash',
        'title': 'About Post',
        'content': 'Second',
        'date_posted': 'August 27, 2018'
    }

]

def home(resquest):
    context = {
        'posts': Post.objects.all()
    }
    return render(resquest, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})