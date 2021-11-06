from django.contrib import admin
from .models import Courses, Lecturers, Comments
# Register your models here.



admin.site.register(Courses)
admin.site.register(Lecturers)

class CommentsAdmin(admin.ModelAdmin):
    list_display =['lecturee_id', 'name', 'email', 'comments']
    

admin.site.register(Comments, CommentsAdmin)