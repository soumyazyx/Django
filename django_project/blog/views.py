from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author': 'CoreyMS',
        'title': 'title1',
        'content': 'content1',
        'date_posted': '2019-11-25'
    },
    {
        'author': 'SoumyaRD',
        'title': 'title2',
        'content': 'content2',
        'date_posted': '2019-11-26'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
