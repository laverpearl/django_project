from django.contrib import admin
from gwamok.models import Sugang


# Register your models here.

@admin.register(Sugang)
class SugangAdmin(admin.ModelAdmin):
    list_display = ('gwamoknum', 'semester', 'name', 'professor', 'day', 'time', 'classroom', 'limitnum')


