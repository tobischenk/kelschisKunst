from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline

from core.models import BaseImage, BaseImageMedium, BaseImageBuyer


class BaseImageMediumInline(TabularInline):
    model = BaseImageMedium
    extra = 0
    fields = ["medium", "created_at", "updated_at"]
    readonly_fields = ["created_at", "updated_at"]


class BaseImageBuyerInline(TabularInline):
    model = BaseImageBuyer
    extra = 0
    fields = ["buyer_persona", "price", "can_be_named"]


@admin.register(BaseImage)
class BaseImageAdmin(ModelAdmin):
    list_display = [
        "file",
        "painting_surface",
        "available_to_buy",
        "price",
    ]
    fields = [
        "file",
        "title",
        "description",
        "started_at",
        "finished_at",
        "width",
        "height",
        "painting_surface",
        "available_to_buy",
        "price",
        "created_at",
        "updated_at"
    ]
    readonly_fields = ["created_at", "updated_at"]
    inlines = [BaseImageMediumInline, BaseImageBuyerInline]
