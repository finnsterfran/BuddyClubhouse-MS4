from django.test import TestCase
from .models import Dog


class TestDogViews(TestCase):
    def test_get_dogs_page(self):
        response = self.client.get('/dogs/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dogs/dogs.html')
