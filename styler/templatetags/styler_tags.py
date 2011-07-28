from django import template
register = template.Library()
import styler.colour as col
import Image, ImageDraw, ImageFont, ImageFilter
from settings import MEDIA_ROOT, SITE_ROOT

@register.simple_tag
def blend(bg, fg, alpha):
    return col.blend(bg,fg,alpha)


@register.simple_tag
def make_rounded_top(cr) :
    return """-webkit-border-top-left-radius:%spx;
-webkit-border-top-right-radius:%spx;
-moz-border-radius-topleft:%spx;
-moz-border-radius-topright:%spx;""" % (cr,cr,cr,cr)

@register.simple_tag
def make_rounded_left(cr) :
    return """-webkit-border-top-left-radius:%spx;
-webkit-border-bottom-left-radius:%spx;
-moz-border-radius-topleft:%spx;
-moz-border-radius-bottomleft:%spx;""" % (cr,cr,cr,cr)

@register.simple_tag
def make_rounded_bottom(cr) :
    return """-webkit-border-bottom-left-radius:%spx;
-webkit-border-bottom-right-radius:%spx;
-moz-border-radius-bottomleft:%spx;
-moz-border-radius-bottomright:%spx;""" % (cr,cr,cr,cr)

@register.simple_tag
def make_rounded(cr) :
    return '-webkit-border-radius: %spx;\n-moz-border-radius: %spx;\n' % (cr,cr)


