from django.http import HttpResponseRedirect
from django.template import RequestContext
from yaos_products.models import Category


def add_common_vars(request, d):
    d['is_logged'] = request.user.is_authenticated()
    d['categories'] = Category.objects.all()
    d['current_user'] = request.user
    return d
