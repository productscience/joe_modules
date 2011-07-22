from django import template
from slides.models import Slide

register = template.Library()

@register.inclusion_tag('slides/includes/slideshow.html')
def slideshow():
    """Render a crossfading slideshow"""

    c = {}

    return c
