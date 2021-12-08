from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User


class TestProfileModel(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='looloo', password='yo!4password')

    def test_can_create_profile(self):
        profile = Profile(
            user=self.user,
            first_name='Lola',
            last_name='Montez',
            username='looloo',
            email='looloo@email.com',
            address_line_1='South Beach Street 99',
            address_line_2='',
            postal_code='23459RR',
        )
        self.assertEqual(profile.user.username, 'looloo')
        self.assertEqual('looloo', str(profile))
