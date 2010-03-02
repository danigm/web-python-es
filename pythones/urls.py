from os import path

from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'main.views.index'),
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(.*)$', 'django.views.static.serve',
         {'document_root': path.join(settings.BASEDIR, 'media')}),
    )
