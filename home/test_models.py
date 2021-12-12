from django.test import TestCase
from .models import ContactUs


class Testmodels(TestCase):
    def test_contactus_str_method_returns_name(self):
        contact = ContactUs.objects.create(name='looloo')
        self.assertEqual(str(contact), 'looloo')
