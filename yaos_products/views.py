from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from yaos_products.models import Product, Category, ShoppingCart
from yaos_home.utils import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def products_from_category(request, name):
    return render_to_response('products_from_category.html', add_common_vars(request, {'products': Product.objects.filter(category__name=name),'category_name':name, } ), context_instance=RequestContext(request))

def all_products(request):
    return render_to_response('products.html', add_common_vars(request, {'products': Product.objects.all(), } ), context_instance=RequestContext(request))

def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render_to_response('product_details.html', add_common_vars(request, {'product': product, }), context_instance=RequestContext(request))

@login_required(login_url='/accounts/login')
def add_to_cart(request):
    if request.method == 'POST':
        product_to_add = get_object_or_404(Product, pk=request.POST['id_of_product'])
        buyer = get_object_or_404(User, pk=request.POST['id_of_user'])
        cart_item = ShoppingCart(user=buyer, product=product_to_add)
        cart_item.save()
        return HttpResponseRedirect("/") 

@login_required(login_url='/accounts/login')
def ordered_products(request):
    user_products = ShoppingCart.objects.filter(user__id=request.user.id)
    return render_to_response('products_in_cart.html', add_common_vars(request, {'cart_items': user_products, } ), context_instance=RequestContext(request))
    
@login_required(login_url='/accounts/login')
def remove_from_cart(request):
    if request.method == 'POST':
        to_remove = get_object_or_404(ShoppingCart, pk=request.POST['id_of_cart_item'])
        to_remove.delete()
        return HttpResponseRedirect("/products/incart") 

