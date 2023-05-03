from django.contrib import admin
from .models import Currency


@admin.register(Currency)
class AdminCurrency(admin.ModelAdmin):
    list_display = ["name", "symbol", "rate"]
    list_editable = ["symbol", "rate"]
