from django.test import TestCase
from .models import Donation


class TestDonationViews(TestCase):
    def test_get_donation_page(self):
        response = self.client.get('/contribution/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contribution/contribution.html')
