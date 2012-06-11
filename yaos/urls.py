from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('yaos_home.urls')),
    url(r'accounts/', include('yaos_auth.urls')),
    url(r'products/', include('yaos_products.urls')), 
)
