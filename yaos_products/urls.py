from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
        url(r'category/$', products_from_category),
)
