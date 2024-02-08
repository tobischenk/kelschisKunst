from django.contrib import admin
from unfold.admin import ModelAdmin

from showroom.models import ShowroomImage


@admin.register(ShowroomImage)
class ShowroomImageAdmin(ModelAdmin):
    fields = ["image", "publish_at", "public", "created_at", "updated_at"]
    list_display = ["image", "publish_at", "public"]
    readonly_fields = ["created_at", "updated_at"]