import os

from django import template
from django.conf import settings

import Image as pil

register = template.Library()


@register.simple_tag
def resize_image(image, width, height, force=True):

    try:
        path = str(image)
    except AttributeError:
        return None

    if not path:
        return None

    # get or create name of cache directory
    dirname = os.path.dirname(path)
    cache_directory = ("/%s/resized_%d_%d" %
                       (dirname, width, height)).replace("//", "/")
    cache_path = cache_directory
    try:
        if not os.path.exists(settings.MEDIA_ROOT + "/" + cache_path):
            os.mkdir(settings.MEDIA_ROOT + "/" + cache_path)
    # this means there is no directory where the original image was meant to
    # be -- image has been deleted? Quit
    except OSError:
        return None

    # get full path to thumb
    thumb_filename = "%d_%d_%s" % (width, height, path.split("/")[-1])
    path_to_thumb = settings.MEDIA_ROOT + \
        "/" + cache_path + "/" + thumb_filename

    # get url of thumb
    thumb_url = settings.MEDIA_URL + cache_directory + "/" + thumb_filename

    # attempt to open cached image
    if os.path.exists(path_to_thumb):
        return thumb_url

    # create the resized image
    path_to_original = settings.MEDIA_ROOT + "/" + path

#    print "path_to_original", path_to_original

    try:
        img = pil.open(path_to_original)
    except IOError:  # file has been deleted?
        return None

    if not force:
        img.thumbnail((width, height), pil.ANTIALIAS)
    else:
        src_width, src_height = img.size
        src_ratio = float(src_width) / float(src_height)
        dst_width, dst_height = width, height
        dst_ratio = float(dst_width) / float(dst_height)

        if dst_ratio < src_ratio:
            crop_height = src_height
            crop_width = crop_height * dst_ratio
            x_offset = float(src_width - crop_width) / 2
            y_offset = 0
        else:
            crop_width = src_width
            crop_height = crop_width / dst_ratio
            x_offset = 0
            y_offset = float(src_height - crop_height) / 3
        img = img.crop(
            (x_offset, y_offset, x_offset + int(crop_width), y_offset + int(crop_height)))
        img = img.resize((dst_width, dst_height), pil.ANTIALIAS)

    img.save(path_to_thumb)

    return thumb_url
