from django.contrib import admin

# Register your models here.
from .models import Blog,Video

admin.site.register(Blog)
admin.site.register(Video)