from ads.models import *
from django.contrib import admin

class PageAdAdmin(admin.ModelAdmin):
    list_display = ['headline', 'active_from', 'active', 'priority', 'pin_to_slot']

admin.site.register(PageAd, PageAdAdmin)
