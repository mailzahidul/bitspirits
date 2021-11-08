from django.shortcuts import render
from .models import Welcome_text
from academics.models import Courses, Lecturers

# Create your views here.

def home(request):
    obj = Welcome_text.objects.get()
    courses = Courses.objects.all()
    lecturers = Lecturers.objects.all()
    context = {
        'text':obj,
        'courses':courses,
        'lecturers':lecturers
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


