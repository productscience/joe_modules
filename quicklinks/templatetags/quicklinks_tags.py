
from django import template
from quicklinks.models import *

register = template.Library()

@register.simple_tag
def render_quicklinks():

    quicklinks = QuickLink.objects.all()
    return "".join(["<li><a href='%s' title='%s'>%s</a></li>" % (q.url, q.mouse_over, q.menu_name) for q in quicklinks])

