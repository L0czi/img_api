from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Account, Tier, Image, Size

# Register your models here.


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'tier',)
    list_filter = ('tier',)

@admin.register(Tier)
class TiersAdmin(admin.ModelAdmin):
    list_display = ('tier_name','display_sizes','generate_orginal_link','generate_expire_link')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner')

admin.site.register(Size)