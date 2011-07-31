from django.db import models


class QuickLink(models.Model):
    menu_name = models.CharField(max_length=15)
    mouse_over = models.CharField(max_length=70, null=True, blank=True, help_text="E.g. 'find out how to join IASO as an individual or company'")
    url = models.CharField(max_length=200, help_text="Enter the url to link to. Either on this site ('/publications') or external ('http://www.bbc.co.uk')")
    order = models.IntegerField(null=True,blank=True)
    def __unicode__(self):
        return self.menu_name
    class Meta :
        ordering = ['order']


# Create your models here.
