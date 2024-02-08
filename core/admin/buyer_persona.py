from django.contrib import admin
from unfold.admin import ModelAdmin

from core.models import BuyerPersona


@admin.register(BuyerPersona)
class BuyerPersonaAdmin(ModelAdmin):
    list_display = ["first_name", "last_name", "email"]
    search_fields = ["first_name", "last_name", "email"]
    fields = ["first_name", "last_name", "email", "created_at", "updated_at"]
    readonly_fields = ["created_at", "updated_at"]
