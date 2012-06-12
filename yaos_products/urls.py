from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
        url(r'category/$', products_from_category),
        url(r'^all', all_products),
        url(r'^(?P<product_id>\d+)/$', product_details),
)
