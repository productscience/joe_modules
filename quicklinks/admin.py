from quicklinks.models import *
from django.contrib import admin

class QuickLinkAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'order', 'url']


admin.site.register(QuickLink, QuickLinkAdmin)
