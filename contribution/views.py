from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.conf import settings
from django.contrib import messages
from .models import Donation


def contribution(request):
    """a view to show donation plans for purchasing"""

    products = Donation.objects.all().order_by('price')

    context = {
        'products': products
    }
    return render(request, 'contribution/contribution.html', context)


def cart(request):
    """ a view to show cart"""
    return render(request, 'contribution/cart.html')


def add_to_cart(request, item_id):
    """ Add quantity of selection to the cart"""
    product = get_object_or_404(Donation, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    messages.success(request, f'You added {quantity} X {product.name} to cart')
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Add or Remove items from the cart"""

    product = get_object_or_404(Donation, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request,
                        (f'Updated {product.name} to {cart[item_id]}'))

    else:
        cart.pop(item_id)
        messages.success(request, (f'Removed {product.name} from your cart'))

    request.session['cart'] = cart
    return redirect(reverse('cart'))
