from django.shortcuts import render
from .models import Welcome_text

# Create your views here.

def home(request):
    obj = Welcome_text.objects.get()
    context = {
        'text':obj
    }
    return render(request, 'pages/index.html', context)



def about(request):
    return render(request, 'pages/about.html')


def gallery(request):
    return render(request, 'pages/gallery.html')


def news(request):
    return render(request, 'pages/news.html')


def event(request):
    return render(request, 'pages/event.html')


def contact(request):
    return render(request, 'pages/contact.html')


