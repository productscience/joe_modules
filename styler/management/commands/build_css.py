from django.core.management.base import BaseCommand, CommandError
from settings import MEDIA_ROOT
from django.template.loader import get_template
from django.template import Context
from styler.palettes import *

class Command(BaseCommand):
    args = ''
    help = 'builds the static css files using templates.'

    def handle(self, *args, **options):
        
        warning = "/* THIS FILE IS AUTOGENERATED. DO NOT EDIT. USE TEMPLATE INSTEAD!! */\n\n\n\n"
        
        for palette, name in [  (MAIN, 'main'),
                                (TINY, 'tiny_styles'),
                             ] :
            c = Context()
            c.update(palette)
            t = get_template('styler/%s.css' % name)
            the_file = open("%s/css/%s.css" % (MEDIA_ROOT, name), 'w')
            the_file.write(warning + t.render(c))
            the_file.close()
        
        print "Finished!"
