from django.db import models
from ads.settings import *
import datetime


slot_choices = [(s[0],s[1]) for s in SLOTS]

class PageAd(models.Model):
    headline = models.CharField(max_length=50, help_text="Write a short headline to advertise the page")
    short_lead = models.CharField(max_length=90, help_text="The first sentence. In a nutshell. 70 characters. Note, if you have a long headline, you may need to cut this even more to make it fit the home-page ad boxes.")
    long_lead = models.CharField(max_length=210, help_text="Alternative lead. Used if there is more room, and on the main page for the advert. 210 characters.")
    image = models.ImageField(upload_to="uploads/page_ad_images", max_length=300, help_text="Page ads must have images. Choose an image as close to square as possible. It will be reduced automatically to fit.")
    active_from = models.DateField(help_text="Usually just today's date. But you can delay this ad appearing if you want to.")
    active_until = models.DateField(help_text="Use this to stop a page ad. An empty date will keep it open. Yesterday's date (or earlier) will stop the ad showing now. A future date will close it automatically at the end of that day.",  null=True, blank=True)
    priority = models.IntegerField(choices=PRIORITIES, help_text="Higher priority ads are more likely to show", default=2)
    pin_to_slot = models.IntegerField(choices=slot_choices, null=True, blank=True, help_text="You can force this page ad to show in a particular position on the home page. If more than one page-ad or action is pinned to the same slot, a random choice will be made.")
    page = models.ForeignKey("cms.page", help_text="Select which web page you want to link to")
    def __unicode__(self):
        return self.headline
    def active(self):
        today = datetime.date.today()
        if self.active_from <= today :
            if not self.active_until or self.active_until >= today :
                return True
        return False
    def get_absolute_url(self):
        return self.page.get_absolute_url()
    active.boolean = True
