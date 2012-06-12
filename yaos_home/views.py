from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from yaos_products.models import Category, Product
from yaos_home.utils import *


def home(request):
    return render_to_response("recent.html", add_common_vars(request, {'products': Product.objects.all().order_by('-pub_date')[:5],}), context_instance=RequestContext(request))

