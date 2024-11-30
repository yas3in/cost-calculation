from django.contrib import admin
from django.contrib.admin import register
from calculation.models import Calculater, Ticket


@register(Calculater)
class CalculaterAdmin(admin.ModelAdmin):
    list_display = ['user', 'cost', 'date', 'description']


@register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("user", "ticket_type", "ticket")
    list_filter = ["ticket_type"]