from django.test import TestCase


class TestHomeViews(TestCase):

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_get_about_page(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_get_contactus_page(self):
        response = self.client.get('/contact_us/')
        self.assertEqual(response.status_code, 200)
