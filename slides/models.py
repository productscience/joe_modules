from django.db import models
from slides.settings import PAGE_MODEL, IMAGE_UPLOAD_DIR
import datetime

class Slide(models.Model):
    headline = models.CharField(max_length=50)
    caption = models.CharField(max_length=180)
    image = models.ImageField(upload_to=IMAGE_UPLOAD_DIR, max_length=300, help_text="Slides must have images. Choose an image as close to square as possible. It will be reduced automatically to fit.")
    mouseover = models.CharField(max_length=100, help_text="Appears when mouse hovers over the slide. E.g. use for photo-credit.", null=True, blank=True)
    colour = models.CharField(max_length=10, null=True, blank=True, help_text="Background colour of slide. Enter a css colour such as '#123456'")
    page = models.ForeignKey(PAGE_MODEL, help_text="Select which web page you want to link to")
    ordering = models.IntegerField(null=True, blank=True)
    show_from = models.DateField(help_text="Click today to start showing this slide immediately")
    show_until = models.DateField(null=True, blank=True, help_text="You can enter an expiry date if you want to")
    def __unicode__(self) :
        return self.headline
    class Meta :
        ordering = ['ordering']
    def active(self) :
        today = datetime.date.today()
        return self.show_from <= today and (self.show_until == None or self.show_until >= today)
    active.boolean = True
    def until(self) :
        if self.show_until :
            return self.show_until.strftime("%B %d, %Y")
        else :
            return ""


