from django.shortcuts import render, redirect
from .models import Welcome_text, Newsletter, Contact, Institution
from .forms import ContactForm
from academics.models import Courses, Lecturers
from article.models import News, Event
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.

def home(request):
    obj = Welcome_text.objects.get()
    courses = Courses.objects.all()
    lecturers = Lecturers.objects.all()
    news = News.objects.all()[:3]
    event = Event.objects.all()[:2]
    context = {
        'text':obj,
        'courses':courses,
        'lecturers':lecturers,
        'news':news,
        'event':event
    }
    return render(request, 'pages/index.html', context)



def about(request):
    lecturers = Lecturers.objects.all()
    context = {
        'lecturers':lecturers
    }
    return render(request, 'pages/about.html', context)


def contact(request):
    forms = ContactForm()
    if request.method == "POST":
        forms = ContactForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, "Your message is submitted successfully.", extra_tags='alert-success')
            return redirect('contact')
        else:
            messages.error(request, forms.errors, extra_tags='alert-danger')
    context = {
        'forms':forms
    }
    return render(request, 'pages/contact.html', context)


def newsletter(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')
        if mail is not None:
            newsletter_create = Newsletter.objects.create(newsletter_mail=mail)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return HttpResponseRedirect("")

