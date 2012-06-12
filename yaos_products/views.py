from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from yaos_products.models import Product
from yaos_home.utils import *

def products_from_category(request):
    pass

def all_products(request):
    return render_to_response('products.html', add_common_vars(request, {'products': Product.objects.all(), } ), context_instance=RequestContext(request))

def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render_to_response('product_details.html', add_common_vars(request, {'product': product, }), context_instance=RequestContext(request))
