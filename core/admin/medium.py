from django.contrib import admin
from unfold.admin import ModelAdmin

from core.models import ImageMedium


@admin.register(ImageMedium)
class ImageMediumAdmin(ModelAdmin):
    list_display = ["name"]
    fields = ["name", "description", "created_at", "updated_at"]
    readonly_fields = ["created_at", "updated_at"]
