from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from yaos_products.models import Product
from yaos_home.utils import *

def products_from_category(request):
    pass

def all_products(request):
    return render_to_response('products.html', add_common_vars(request, {'products': Product.objects.all(), } ), context_instance=RequestContext(request))
