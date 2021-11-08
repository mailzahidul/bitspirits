from .models import Institution


def institute(request):
    inst_obj = Institution.objects.get(id=1)
    context = {
        'institute':inst_obj
    }
    return context