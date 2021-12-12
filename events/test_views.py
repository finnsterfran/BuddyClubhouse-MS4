from django.test import TestCase


class TestHomeViews(TestCase):

    def test_get_events_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
