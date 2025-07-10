from django.contrib import admin

# Register your models here.
from .models import AllCourses, Details

admin.site.register(AllCourses)
admin.site.register(Details)
