from django.shortcuts import render, redirect
from .models import Lecturers, Comments, Courses, CourseCategory
from django.views import View
from django.db.models import Q
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.



def courses(request):
    # course_name = request.GET.get('course_name')
    # result  = Courses.objects.filter(
    #         Q(course_title__icontains=course_name) | 
    #         Q(short_description__icontains=course_name) | 
    #         Q(description__icontains=course_name)
    #         )

    all_courses = Courses.objects.all()
    context ={
        'courses': all_courses
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
        mail_address = lec_obj.email
        subject = "An Email from Your Academi"
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST.get('comments')
        # The message will save to database and mail also to perticular lecturer
        if name and email and comment:
            obj = Comments.objects.create(lecturee_id=lec_obj, name=name, email=email, comments = comment)
            send_mail(subject+" from "+name, comment, email, [mail_address], fail_silently=False)
            messages.success(request, "Your message is send successfully.", extra_tags='alert-success')
        return redirect('lecturer', lec_obj.id)