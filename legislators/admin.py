from django.contrib import admin
from .models import Legislator

# Register your models here.
@admin.register(Legislator)
class LegislatorAdmin(admin.ModelAdmin):
    ordering = ('last_name',)
    list_filter = ('in_office', 'chamber',)


