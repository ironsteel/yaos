from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('yaos_home.urls')),
    url(r'accounts/', include('yaos_auth.urls')),
    url(r'products/', include('yaos_products.urls')), 
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
            
)
