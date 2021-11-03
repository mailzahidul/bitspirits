from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'pages/index.html')



def about(request):
    return render(request, 'pages/about.html')


def gallery(request):
    return render(request, 'pages/gallery.html')


def courses(request):
    return render(request, 'pages/courses.html')


def lecturers(request):
    return render(request, 'pages/lecturers.html')


def news(request):
    return render(request, 'pages/news.html')


def event(request):
    return render(request, 'pages/event.html')


def contact(request):
    return render(request, 'pages/contact.html')


