from django.shortcuts import render, redirect
from .models import Lecturers, Comments, Courses, CourseCategory
from django.views import View
from django.db.models import Q
from django.core.mail import send_mail
# Create your views here.



def courses(request):
    # course_name = request.GET.get('course_name')
    # result  = Courses.objects.filter(
    #         Q(course_title__icontains=course_name) | 
    #         Q(short_description__icontains=course_name) | 
    #         Q(description__icontains=course_name)
    #         )

    all_courses = Courses.objects.all()
    categories = CourseCategory.objects.all()
    context ={
        'courses': all_courses,
        'categories': categories
    }
    return render(request, 'pages/courses.html', context)


def course(request, id):
    try:
        course_view = Courses.objects.get(id=id)
        teachers = course_view.assigned_teacher.all()
        context={
            'course':course_view,
            'teachers':teachers
        }
        return render(request, 'pages/course_view.html', context)
    except Exception as err:
        print(err)
        return redirect('home')

def lecturers(request):
    all_lecturers = Lecturers.objects.all()
    context = {
        'lecturers':all_lecturers
    }
    return render(request, 'pages/lecturers.html', context)

class Lecturee(View):
    def get(self, request, id):
        lecturer_obj = Lecturers.objects.get(id=id)
        context={
            'lecturer': lecturer_obj
        }
        return render(request, 'pages/lecturer_view.html', context)
    
    def post(self, request, id):
        lec_obj = Lecturers.objects.get(id=id)
        lec_id = request.POST.get('lecturer')
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST.get('comments')
        obj = Comments.objects.create(lecturee_id=lec_id, name=name, email=email, comments = comment)
        # send_mail('Query from website '. name, comment, email, ['to@example.com'], fail_silently=False)
        return redirect('lecturer', lec_obj.id)



def news(request):
    return render(request, 'pages/news.html')



def event(request):
    return render(request, 'pages/event.html')