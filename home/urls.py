from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('courses/', views.courses, name='courses'),
    path('lecturers/', views.lecturers, name='lecturers'),
    path('news/', views.news, name='news'),
    path('event/', views.event, name='event'),
    path('contact/', views.contact, name='contact'),
]