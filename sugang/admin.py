from django.contrib import admin
from sugang.models import Sugang



@admin.register(Sugang)
class SugangAdmin(admin.ModelAdmin):
    list_display = ('name', 'professor')
    