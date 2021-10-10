from django.contrib import admin
from student.models import Student


# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('studentnum', 'name', 'department', 'tel', 'email', 'address')


