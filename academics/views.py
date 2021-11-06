from django.shortcuts import render, redirect
from .models import Lecturers, Comments
from django.views import View
# Create your views here.



def courses(request):
    return render(request, 'pages/courses.html')



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
        return redirect('lecturer', lec_obj.id)