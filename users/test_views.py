from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from users.forms import CustomUserCreationForm

User = get_user_model()


class TestViews(TestCase):

    def setUp(self):
        self.registration_form = CustomUserCreationForm({
            'first_name': 'Lola',
            'last_name': 'Montez',
            'email': 'looloo@email.com',
            'username': 'looloo',
            'password1': 'yo!4password',
            'password2': 'yo!4password',
        })
        self.data = {
            'first_name': 'Lola',
            'last_name': 'Montez',
            'email': 'looloo@email.com',
            'username': 'looloo',
            'password1': 'yo!4password',
            'password2': 'yo!4password',
        }

    def test_get_register_page(self):
        response = self.client.get('/users/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login_register.html')

    def test_new_user_is_registered(self):
        existing_users = User.objects.count()
        self.client.post(reverse('register'), self.data)
        new_users_made = User.objects.count()
        self.assertEqual(new_users_made, existing_users + 1)

    def test_get_account_page(self):
        user = User.objects.create_user(username='looloo',
                                        password='yo!4password')
        self.client.login(username='looloo', password='yo!4password')
        response = self.client.get('/users/account/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/account.html')

    def test_get_login_page(self):
        response = self.client.get('/users/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login_register.html')

    def test_registered_user_login(self):
        self.registration_form.save()
        login_okay = self.client.login(username='looloo',
                                       password='yo!4password')
        self.assertTrue(login_okay)

    def test_logout_function(self):
        self.registration_form.save()
        login_okay = self.client.login(username='looloo',
                                       password='yo!4password')
        self.assertTrue(login_okay)
        response = self.client.get('/users/logout/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/users/login/')
