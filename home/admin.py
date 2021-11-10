from django.contrib import admin
from .models import Welcome_text, Institution, Newsletter, Contact

# Register your models here.


admin.site.register(Welcome_text)
admin.site.register(Institution)
admin.site.register(Newsletter)
admin.site.register(Contact)
