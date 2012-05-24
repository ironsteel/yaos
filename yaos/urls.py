from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yaos.views.home', name='home'),
    # url(r'^yaos/', include('yaos.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
   

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', direct_to_template, {'template': 'base.html'}, name="index"),
    url(r'accounts/', include('yaos_auth.urls')),

)
