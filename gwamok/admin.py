from django.contrib import admin
from gwamok.models import Gwamok


# Register your models here.

@admin.register(Gwamok)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('gwamoknum', 'semester', 'name', 'professor', 'day', 'time', 'classroom', 'limitnum')

