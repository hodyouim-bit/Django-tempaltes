from django.contrib import admin
from .models import student, Major

@admin.register(student)
class student_ADMIN(admin.ModelAdmin):
    list_filter = ()    
    list_display = ('st_id', 'prefix', 'fname', 'lname', 'mj_id')

@admin.register(Major)
class admin_major(admin.ModelAdmin):
    list_display = ("mj_name",)


