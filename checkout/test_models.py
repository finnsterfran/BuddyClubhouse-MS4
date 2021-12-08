from django.test import TestCase
from .models import Order, OrderLineItem
from contribution.models import Donation


class TestOrderCheckoutModel(TestCase):
    def test_checkout_billing_address(self):
        billing_address = Order(
            first_name='Lola',
            last_name='Montez',
            email='looloo@email.com',
            address_line_1='South Beach Street 99',
            address_line_2='',
            postal_code='23459RR')
        
        self.assertEqual(billing_address.first_name, 'Lola')
        self.assertEqual(billing_address.last_name, 'Montez')
        self.assertEqual(billing_address.email, 'looloo@email.com')
        self.assertEqual(billing_address.address_line_1, 'South Beach Street 99')
        self.assertEqual(billing_address.address_line_2, '')
        self.assertEqual(billing_address.postal_code, '23459RR')
    
    def test_put_in_an_order(self):
        order = Order(order_total=85.00)
        order.save()
        self.assertEqual(order.order_total, 85.00)


class TestOrderLineItemCheckout(TestCase):
    def test_check_order_exists(self):
        order_number = Order(id=1, order_total=345.00)
        order_number.save()
        product = Donation(name="Test Donation", price=345.00)
        product.save()
        orderLineItem = OrderLineItem(product=product,
                                      quantity=1,
                                      order=order_number)
        orderLineItem.save()
        self.assertEqual(orderLineItem.product, product)
        self.assertEqual(orderLineItem.quantity, 1)
        self.assertEqual(orderLineItem.lineitem_total, 345.00)
