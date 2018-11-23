from django.shortcuts import render
 
# Create your views here.

posts = [
    {
        'author': 'Vinay',
        'title': 'Post 1',
        'content': 'Hello from the other side',
        'date_posted': 'November 23 2018'
    },
    {
        'author': 'Mr Robot',
        'title': 'Post 2',
        'content': 'Hello from the anti side',
        'date_posted': 'November 23 2018'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', { 'title': 'About'})