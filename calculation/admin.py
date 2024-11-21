from django.contrib import admin
from django.contrib.admin import register
from calculation.models import Calculater


@register(Calculater)
class CalculaterAdmin(admin.ModelAdmin):
    list_display = ['user', 'cost', 'date', 'description']
