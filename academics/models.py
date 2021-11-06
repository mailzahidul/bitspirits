from django.db import models

# Create your models here.

class Lecturers(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    image = models.ImageField(upload_to='lecturers/')
    about = models.TextField()
    qualification = models.TextField()
    email = models.EmailField()
    linkdin = models.URLField(max_length=200, blank=True, null=True)
    twetter = models.URLField(max_length=200, blank=True, null=True)
    facebook = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name




class Courses(models.Model):
    course_title = models.CharField(max_length=50)
    short_description = models.TextField()
    description = models.TextField()
    feature_img = models.ImageField(upload_to='courses/', blank=True, null=True)
    fees = models.PositiveIntegerField()
    featured = models.BooleanField(default=False)
    assigned_teacher = models.ForeignKey(Lecturers, on_delete=models.SET_NULL, null=True)
    duration = models.CharField(max_length=20, blank=True, null=True)
    classes = models.CharField(max_length=20, blank=True, null=True)
    time = models.CharField(max_length=20, blank=True, null=True)
    lecture = models.CharField(max_length=20, blank=True, null=True)
    lecture_question = models.CharField(max_length=20, blank=True, null=True)
    lecture_description = models.TextField(blank=True, null=True)
    lecture_duration = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.course_title


class Comments(models.Model):
    lecturee_id = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    comments = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.lecturee_id + self.name
