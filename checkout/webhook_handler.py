from django.http import HttpResponse
from .models import Order, OrderLineItem
from contribution.models import Donation
import json
import time


class StripeWH_Handler:
    """
    handle Stripe webhooks
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}', status=200)

    def handle_payment_intent_succeed(self, event):
        """
        handle the payment_intent.succeeded webhook from Stripe
        """
        # Create order in event form was not submitted for some reason or other
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    first_name__iexact=shipping_details.name.split()[0],
                    last_name__iexact=shipping_details.name.split()[1],
                    email__iexact=billing_details.email,
                    postcode__iexact=shipping_details.address.postal_code,
                    address_line_1__iexact=shipping_details.address.line1,
                    address_line_2__iexact=shipping_details.address.line2,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                    content=(f'Webhook received: {event["type"]} | SUCCESS: '
                    'Verified order already in database'),
                    status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    first_name=shipping_details.name.split()[0],
                    last_name=shipping_details.name.split()[1],
                    email=billing_details.email,
                    postal_code=shipping_details.address.postal_code,
                    address_line_1=shipping_details.address.line1,
                    address_line_2=shipping_details.address.line2,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(cart).items():
                    product = Donation.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        return HttpResponse(
            content=(f'Webhook received: {event["type"]} | SUCCESS: '
                     'Created order in webhoook'),
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)


