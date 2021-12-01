from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
from .models import Donation


def contribution(request):
    """ A view to show donation plans available """
    products = Donation.objects.all().order_by('price')
    context = {
        'products': products
    }
    return render(request, 'contribution/contribution.html', context)


def cart(request):
    """ A view to show shopping cart """
    return render(request, 'contribution/cart.html')


def add_to_cart(request, item_id):
    """ Add quantity of selection to the cart """
    product = get_object_or_404(Donation, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity
    
    request.session['cart'] = cart
    return redirect(redirect_url)