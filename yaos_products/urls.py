from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
        url(r'category/(?P<name>\w{0,50})/$', products_from_category),
        url(r'^all', all_products),
        url(r'^(?P<product_id>\d+)/$', product_details),
        url(r'^add_to_cart', add_to_cart),
        url(r'^incart', ordered_products),
)
