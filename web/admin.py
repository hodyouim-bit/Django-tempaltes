from django.contrib import admin
from .models import student

@admin.register(student)
class student_ADMIN(admin.ModelAdmin):
    list_filter = ()    
    list_display = ('st_id', 'prefix', 'fname', 'lname')
