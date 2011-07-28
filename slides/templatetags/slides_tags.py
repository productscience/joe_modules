from django import template
from slides.models import Slide
import datetime
from django.conf import settings
from slides.settings import *


register = template.Library()

@register.inclusion_tag('slides/includes/slideshow.html')
def slideshow():

    """Render a crossfading slideshow"""

    today = datetime.date.today()
    slides = Slide.objects.filter(show_from__lte=today).exclude(show_until__lt=today)     #TODO: Add show_until if not blank

    return { 'slides' : slides,
             'MEDIA_URL' : settings.MEDIA_URL,
             'image_x' : IMAGE_X,
             'image_y' : IMAGE_Y,
             'total_x' : TOTAL_X,
             'pad_left' : PAD_LEFT,
             'pad_right' : PAD_RIGHT,
             'pad_top' : PAD_TOP,
             'info_x' : TOTAL_X - IMAGE_X - PAD_LEFT - PAD_RIGHT,
             'info_y' : IMAGE_Y - PAD_TOP,
             'nav_inactive_col' : NAV_INACTIVE_COLOUR,
             'nav_active_col' : NAV_ACTIVE_COLOUR,}
