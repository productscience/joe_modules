from django.db import models
from blog.settings import USER_MODEL

#assumes tinymce installed
from tinymce.models import HTMLField


class Category(models.Model):
    name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name
    class Meta :
        ordering = ['name']
        verbose_name_plural = "Categories"


class Post(models.Model):
    author = models.ForeignKey(USER_MODEL)
    date = models.DateField()
    categories = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    content = HTMLField()
    def __unicode__(self):
        return self.title
    class Meta :
        ordering = ['-date']
