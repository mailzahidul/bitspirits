from django.contrib import admin
from .models import News, Category, Comments, Event, EventRegistration
# Register your models here.


admin.site.register(News)
admin.site.register(Category)
admin.site.register(Comments)
admin.site.register(Event)
admin.site.register(EventRegistration)
