from django import template
from slides.models import Slide
import datetime

register = template.Library()

@register.inclusion_tag('slides/includes/slideshow.html')
def slideshow():

    """Render a crossfading slideshow"""

    today = datetime.date.today()
    slides = Slide.objects.filter(show_from__gte=today)     #TODO: Add show_until if not blank

    return { 'slides' : slides }
