from django.contrib import admin

# Register your models here.
from .models import Blog,Video,Comment

admin.site.register(Blog)
admin.site.register(Video)
admin.site.register(Comment)