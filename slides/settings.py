from django.conf import settings


#NAMESPACE (can change from "SLIDES_" in case already used)
ns = getattr(settings, "JOE_DJANGO_SLIDES_NAMESPACE", "SLIDES") + "_"


# The page model that slides should link to when clicked. Must have get_absolute_url()
PAGE_MODEL = getattr(settings, ns + "PAGE_MODEL", "cms.page")

# Media folder where uploaded originals should be stored. Relative to MEDIA_ROOT.
IMAGE_UPLOAD_DIR = getattr(settings, ns + "IMAGE_UPLOAD_DIR", "uploads/slide_images/")

# default CSS colour for text background of slide
DEFAULT_BG_COLOUR = getattr(settings, ns + "DEFAULT_BG_COLOUR", "#E8E7DC")



