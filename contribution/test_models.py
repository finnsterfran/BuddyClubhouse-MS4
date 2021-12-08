from django.test import TestCase
from .models import Donation


class TestDonationModel(TestCase):
    def test_string_representation(self):
        product = Donation.objects.create(name='Test Donation',
                                          description='Test Description',
                                          price=85.00)
        self.assertEqual(str(product), product.name)
