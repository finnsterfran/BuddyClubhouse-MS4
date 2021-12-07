from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from users.forms import ProfileForm, CustomUserCreationForm

User = get_user_model

c=Client()
class TestViews(TestCase):

    def registration(self):
        self.registration_form = CustomUserCreationForm({
            'first_name': 'first_name',
            'last_name': 'last_name',
            'email': 'email@email.com',
            'username': 'username',
            'password1': 'pass123word',
            'password2': 'pass123word',
        })