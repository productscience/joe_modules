from django.conf.urls.defaults import *

urlpatterns = patterns('styler.views',
    (r'^auto_([^/]*).css', 'css'),
)

