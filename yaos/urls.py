from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', direct_to_template, {'template': 'base.html'}, name="index"),
    url(r'accounts/', include('yaos_auth.urls')),
)
