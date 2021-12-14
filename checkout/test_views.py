from django.test import TestCase, Client
from django.urls import reverse
from contribution.models import Donation
from django.contrib.auth.models import User
from django.contrib.messages import get_messages


class TestCheckoutView(TestCase):

    def setUp(self):
        self.client = Client()
        self.checkout = reverse('checkout')
        self.user = User.objects.create_user(
            username = 'looloo',
            email = 'looloo@email.com',
            password = 'yo!4password',
        )
        self.item = Donation.objects.create(name='test item',
                                            price='15')
        self.add_to_cart = reverse('add_to_cart',
                                   kwargs={'item_id': self.item.id})


    def test_get_checkout_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_checkout_view_with_empty_cart(self):
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "There is nothing in your bag at the moment")
    
    def test_checkout_view_with_cart(self):
        self.client.post(self.add_to_cart,
                         data={'quantity': '1',
                               'redirect_url': '/'})
        response = self.client.get(self.checkout)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')
        self.assertTemplateUsed(response, 'base.html')
    
    def test_checkout_success(self):
        self.client.post(self.add_to_cart,
                         data={'quantity': '1',
                               'redirect_url': '/'})
        response = self.client.post(self.checkout,
                                    data={
                                        'first_name': 'Lola',
                                        'last_name': 'Montez',
                                        'email': 'looloo@email.com',
                                        'address_line_1': 'South Beach Street 99',
                                        'address_line_2': '',
                                        'postal_code': '23459RR', 
                                        'client_secret': 'client',
                                        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
    
    def test_checkout_view_with_form_prefilled(self):
        self.client.post(self.add_to_cart, 
                         data={'quantity': '1', 'redirect_url': '/'})
        self.client.login(username='looloo', password='yo!4password')
        response = self.client.get(self.checkout)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['order_form'].initial['email'], self.user.email)
