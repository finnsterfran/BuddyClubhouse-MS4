from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from contribution.models import Donation
from users.models import Profile
import json
import time


class StripeWH_Handler:
    """ Handle Stripe webhooks """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """ Send user a confirmation email """
        customer_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            [customer_email],
            fail_silently=False,
        )

    def handle_event(self, event):
        """ Handle a generic/unknown/unexpected webhook event """
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

        # Update profile information if save_info wwas checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = Profile.objects.get(user__username=username)
            if save_info:
                postal_code = shipping_details.address.postal_code,
                address_line_1 = shipping_details.address.line1,
                address_line_2 = shipping_details.address.line2,
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    first_name__iexact=shipping_details.name.split()[0],
                    last_name__iexact=shipping_details.name.split()[1],
                    email__iexact=billing_details.email,
                    postal_code__iexact=shipping_details.address.postal_code,
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
            self._send_confirmation_email(order)
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
                    username=profile,
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
        self._send_confirmation_email(order)
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
