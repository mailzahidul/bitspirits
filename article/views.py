from django.shortcuts import render
from .models import News, Event, EventRegistration
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
# Create your views here.


def news(request):
    news = News.objects.all()
    events = Event.objects.all()
    context = {
        'news':news,
        'events': events
    }
    return render(request, 'pages/news.html', context)

def news_view(request, id):
    news_obj = News.objects.get(pk=id)
    events = Event.objects.all()
    context = {
        'news':news_obj,
        'events': events
    }
    return render(request, 'pages/news_view.html', context)

def news_search(request):
    search = request.GET.get('search', "None")
    result  = News.objects.filter(
            Q(title__icontains=search) | 
            Q(description__icontains=search)
            )
    print(result, "ssssssssssssssss")
    context = {
        'result':result
    }
    return render(request, 'pages/news_search.html', context)



def event(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'pages/event.html', context)


def event_view(request, id):
    event_obj = Event.objects.get(pk=id)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        website = request.POST['website']
        message = request.POST['message']
        EventRegistration.objects.create(name=name, email=email, website=website, message=message )
        messages.success(request, "Your message is submitted successfully.", extra_tags='alert-success')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {
        'event':event_obj
    }
    return render(request, 'pages/event_view.html', context)



def event_search(request):
    search = request.GET.get('search', "None")
    result  = Event.objects.filter(
            Q(title__icontains=search) | 
            Q(description__icontains=search)
            )
    print(result,"RESSSSS")
    context = {
        'result':result
    }
    return render(request, 'pages/event_search.html', context)

def gallery(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'pages/gallery.html', context)