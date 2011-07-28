from django.conf import settings
from styler.colour import *

#NAMESPACE (can change from "STYLER_" in case already used)
ns = getattr(settings, "JOE_DJANGO_STYLER_NAMESPACE", "STYLER") + "_"

#PALETTE
class Blank() :
    pass
p = Blank()
p.white = '#FFFFFF'
p.black = '#000000'
p.warm_light = '#FFFFCF'
p.light = blend(p.white, p.warm_light, 0.2)
p.ink = '#494949'
p.corner_radius = 8

PALETTE = {}
for attr, value in p.__dict__.iteritems():
    PALETTE[attr] = value

custom_palette = getattr(settings, ns + "PALETTE", None)
if custom_palette :
    PALETTE.update(custom_palette)




