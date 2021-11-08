from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.courses, name='courses'),
    path('course/<int:id>', views.course, name='course'),
    path('lecturers/', views.lecturers, name='lecturers'),
    path('lecturer/<int:id>', views.Lecturee.as_view(), name='lecturer'),
    path('news/', views.news, name="news"),
    path('event/', views.event, name='event')
]