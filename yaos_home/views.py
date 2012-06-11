from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from yaos_products.models import Category
from yaos_home.utils import *


def home(request):
    return render_to_response("index.html", add_common_vars(request, {}), context_instance=RequestContext(request))

