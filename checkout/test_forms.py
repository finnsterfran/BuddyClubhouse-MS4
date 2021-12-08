from django.test import TestCase
from .forms import OrderForm


class TestCheckoutOrderForm(TestCase):

    def test_create_order_with_required_fields(self):
        form = OrderForm({
            'first_name': 'Lola',
            'last_name': 'Montez',
            'email': 'looloo@email.com',
            'address_line_1': 'South Beach Street 99',
            'address_line_2': '',
            'postal_code': '23459RR'
        })
        self.assertTrue(form.is_valid())

    def test_alert_prompt_for_incomplete_form(self):
        form = OrderForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['first_name'][0], 'This field is required.')

