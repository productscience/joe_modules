from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
    (r'^/?$', 'home'),
    (r'^(\d+)/(\d+)/?$', 'show_month'),
    (r'^categories/([^/]*)/?$', 'show_category'),
    (r'^(\d+)/(\d+)/([^/]*)/?$', 'show_post'),

    #(r'^ticker/([^/]*)/$', 'ticker'),
)

