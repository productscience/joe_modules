from django.conf.urls.defaults import *

urlpatterns = patterns('joe_modules.blog.views',
    (r'^/?$', 'blog_home'),
    #(r'^ticker/([^/]*)/$', 'ticker'),
)

