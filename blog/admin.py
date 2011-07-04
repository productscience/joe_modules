
from blog.models import *
from django.contrib import admin


class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ['categories']
    list_display = ['__unicode__', 'author', 'date']

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
