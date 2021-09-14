from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from sorl.thumbnail.admin import AdminImageMixin
from .models import Account, Tier, Image

# Register your models here.


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "tier",
    )
    list_filter = ("tier",)


@admin.register(Tier)
class TiersAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "tier_name",
    )


@admin.register(Image)
class ImageAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ("id", "owner")
