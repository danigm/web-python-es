from os import path

from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('planet.views',
    (r'^$', 'index'),
    (r'^update/', 'update'),
)
