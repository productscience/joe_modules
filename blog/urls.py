from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
    (r'^/?$', 'blog_home'),
    #(r'^ticker/([^/]*)/$', 'ticker'),
)

