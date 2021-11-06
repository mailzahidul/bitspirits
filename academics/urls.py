from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.courses, name='courses'),
    path('lecturers/', views.lecturers, name='lecturers'),
    path('lecturer/<int:id>', views.Lecturee.as_view(), name='lecturer')
]