from django.db import models

# Create your models here.

class Welcome_text(models.Model):
    title = models.CharField(max_length=50)
    short_note = models.TextField()
    image = models.ImageField(upload_to='welcome/')

    def __str__(self):
        return self.title