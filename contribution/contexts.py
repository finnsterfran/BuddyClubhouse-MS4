from django.conf import settings
from django.shortcuts import get_object_or_404
from contribution.models import Donation


def cart_contents(request):
    """
    This makes the cart contents
    can be fetched through the entire project
    """
    cart_items = []
    total = 0
    item_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Donation, pk=item_id)
        total += quantity * product.price
        item_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    grand_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'item_count': item_count,
        'grand_total': grand_total
    }
    return context
