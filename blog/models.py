from django.db import models
from joe_modules.blog.settings import USER_MODEL

class BlogEntry(models.Model):
    author = models.ForeignKey(USER_MODEL)
    test = models.CharField(max_length=20)
