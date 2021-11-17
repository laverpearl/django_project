from django.contrib import admin
from sugang.models import Sugang


# Register your models here.

"""
class SugangInline(admin.StackedInline):
    model = Gwamok
    extra = 1

"""

@admin.register(Sugang)
class SugangAdmin(admin.ModelAdmin):
    #list_display = ('gwamoknum', 'semester', 'name', 'professor', 'day', 'time', 'classroom')
    list_display = ('name', 'professor')
    
"""
@admin.register(Gwamok)
class GwamokAdmin(admin.ModelAdmin):
    list_display = ('gwamoknum', 'semester', 'name', 'professor', 'day', 'time', 'classroom')
"""