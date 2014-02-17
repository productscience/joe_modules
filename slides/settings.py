from django.conf import settings


#NAMESPACE (can change from "SLIDES_" in case already used)
ns = getattr(settings, "JOE_DJANGO_SLIDES_NAMESPACE", "SLIDES") + "_"

# The page model that slides should link to when clicked. Must have get_absolute_url()
PAGE_MODEL = getattr(settings, ns + "PAGE_MODEL", "cms.page")

# Media folder where uploaded originals should be stored. Relative to MEDIA_ROOT.
IMAGE_UPLOAD_DIR = getattr(settings, ns + "IMAGE_UPLOAD_DIR", "uploads/slide_images/")

# Dimensions
IMAGE_X = getattr(settings, ns + "IMAGE_X", 270)
IMAGE_Y = getattr(settings, ns + "IMAGE_Y", 250)
TOTAL_X = getattr(settings, ns + "IMAGE_X", 575)
PAD_TOP = getattr(settings, ns + "PAD_TOP", 15)
PAD_LEFT = getattr(settings, ns + "PAD_LEFT", 30)
PAD_RIGHT = getattr(settings, ns + "PAD_RIGHT", 15)
NAV_INACTIVE_COLOUR = getattr(settings, ns + "NAV_INACTIVE_COLOUR", '#a4a198')
NAV_ACTIVE_COLOUR = getattr(settings, ns + "NAV_ACTIVE_COLOUR", '#172474')



