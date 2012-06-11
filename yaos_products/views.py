from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from yaos_products.models import Product

def products_from_category(request):
    pass

def all_products(request):
    return render_to_response('products.html', {'products': Product.objects.all(), 'is_logged': request.user.is_authenticated(), }, context_instance=RequestContext(request))
