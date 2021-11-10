from django.db import models
from django.contrib.auth.models import User
# Create your models here.


STATUS = (
    ('active', 'Activae'),
    ('deactive', 'Deactivae')
)


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to = "news/", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(choices=STATUS, max_length=10, default='active')
    featured = models.BooleanField(default=False)
    visit_count = models.IntegerField(default=0)
    visible = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    post = models.ForeignKey(News, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    body = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="event/")
    description = models.TextField()
    where_at = models.CharField(max_length=500)
    event_time = models.DateTimeField()
    created_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class EventRegistration(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    website = models.URLField()
    message = models.TextField()
    created_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name



