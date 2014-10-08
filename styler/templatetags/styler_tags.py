from django import template
import styler.colour as col
register = template.Library()

@register.simple_tag
def blend(bg, fg, alpha):
    return col.blend(bg,fg,alpha)


@register.simple_tag
def make_rounded_top(cr) :
    return """-webkit-border-top-left-radius:%spx;
-webkit-border-top-right-radius:%spx;
-moz-border-radius-topleft:%spx;
-moz-border-radius-topright:%spx;
border-top-left-radius:%spx;
border-top-right-radius:%spx;""" % (cr,cr,cr,cr,cr,cr)

@register.simple_tag
def make_rounded_left(cr) :
    return """-webkit-border-top-left-radius:%spx;
-webkit-border-bottom-left-radius:%spx;
-moz-border-radius-topleft:%spx;
-moz-border-radius-bottomleft:%spx;
border-top-left-radius:%spx;
border-bottom-left-radius:%spx;""" % (cr,cr,cr,cr,cr,cr)

@register.simple_tag
def make_rounded_right(cr) :
    return """-webkit-border-top-right-radius:%spx;
-webkit-border-bottom-right-radius:%spx;
-moz-border-radius-topright:%spx;
-moz-border-radius-bottomright:%spx;
border-top-right-radius:%spx;
border-bottom-right-radius:%spx;""" % (cr,cr,cr,cr,cr,cr)

@register.simple_tag
def make_rounded_bottom(cr) :
    return """-webkit-border-bottom-left-radius:%spx;
-webkit-border-bottom-right-radius:%spx;
-moz-border-radius-bottomleft:%spx;
-moz-border-radius-bottomright:%spx;
border-bottom-left-radius:%spx;
border-bottom-right-radius:%spx;""" % (cr,cr,cr,cr,cr,cr)

@register.simple_tag
def make_rounded(cr) :
    return """-webkit-border-radius: %spx;
-moz-border-radius: %spx;
border-radius:%spx;""" % (cr,cr,cr)
