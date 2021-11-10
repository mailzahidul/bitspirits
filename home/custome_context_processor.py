from .models import Institution
from academics.models import CourseCategory


def institute(request):
    inst_obj = Institution.objects.get(id=1)
    context = {
        'institute':inst_obj
    }
    return context


def category_all(request):
    categories =  CourseCategory.objects.all()
    context = {
        'categories':categories
    }
    return context