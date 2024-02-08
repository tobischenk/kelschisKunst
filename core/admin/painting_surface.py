from django.contrib import admin
from unfold.admin import ModelAdmin

from core.models import ImagePaintingSurface


@admin.register(ImagePaintingSurface)
class ImagePaintingSurfaceAdmin(ModelAdmin):
    list_display = ["name"]
    fields = ["name", "description", "created_at", "updated_at"]
    readonly_fields = ["created_at", "updated_at"]
