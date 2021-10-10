from django.contrib import admin
from namecard.models import Namecard


# Register your models here.

@admin.register(Namecard)
class NamecardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'tel', 'company', 'email', 'group')