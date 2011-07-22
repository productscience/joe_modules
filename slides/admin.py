
from slides.models import *
from django.contrib import admin


class SlideAdmin(admin.ModelAdmin):
    list_display = ['__unicode__']

admin.site.register(Slide, SlideAdmin)
