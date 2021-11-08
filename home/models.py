from django.db import models

# Create your models here.

class Welcome_text(models.Model):
    title = models.CharField(max_length=50)
    short_note = models.TextField()
    image = models.ImageField(upload_to='welcome/')

    def __str__(self):
        return self.title


class Institution(models.Model):
    insti_name = models.CharField(max_length=100)
    insti_logo = models.ImageField(upload_to='institute/', blank=True, null=True)
    insti_description = models.TextField(blank=True, null=True)
    insti_phone = models.CharField(max_length=11, blank=True, null=True)
    insti_address = models.CharField(max_length=11)
    insti_email = models.EmailField()
    insti_facebook = models.URLField(max_length=200, blank=True, null=True)
    insti_twitter = models.URLField(max_length=200, blank=True, null=True)
    insti_linkdin = models.URLField(max_length=200, blank=True, null=True)
    insti_pinterest = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.insti_name



class Contact(models.Model):
    name = models.CharField(max_length=80)
    mail = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name



class Newsletter(models.Model):
    newsletter_mail = models.EmailField()

    def __str__(self):
        return self.newsletter_mail
