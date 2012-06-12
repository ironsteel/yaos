from django.http import HttpResponseRedirect
from django.template import RequestContext
from yaos_products.models import Category, ShoppingCart, Product


def add_common_vars(request, d):
    d['is_logged'] = request.user.is_authenticated()
    d['categories'] = Category.objects.all()
    d['current_user'] = request.user
    products_in_cart = ShoppingCart.objects.filter(user__id=request.user.id)
    d['products_in_cart'] = len(products_in_cart)
    total = 0
    for cart_item in products_in_cart:
        total += cart_item.product.price
    d['total'] = total
    return d
