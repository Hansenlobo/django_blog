from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
posts = [
    {
        'author': 'hansen',
        'title': '1st blog',
        'content': 'heloooooooooooooooooo',
        'date_posted': 'august 21,2019',
    },
    {
        'author': 'test user',
        'title': '2st blog',
        'content': 'helooo worlddddd',
        'date_posted': 'august 11,2019',
    }
]
context = {
    'posta': Post.objects.all()
}


def home(request):
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'aboout'})
