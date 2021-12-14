from django.test import TestCase
from .forms import ProfileForm, CustomUserCreationForm


class TestCustomUserCreationForm(TestCase):
    """
    Template for repeated use through the various testing
    """
    def setUp(self):
        self.registration_form = CustomUserCreationForm({
            'first_name': 'Lola',
            'last_name': 'Montez',
            'email': 'looloo@email.com',
            'username': 'looloo',
            'password1': 'yo!4password',
            'password2': 'yo!4password'
        })

    def test_registration_form_incomplete(self):
        form = CustomUserCreationForm({
            'first_name': '',
            'last_name': '',
            'email': '',
            'username': '',
            'password1': '',
            'password2': ''
        })
        self.assertFalse(form.is_valid())

    def test_registration_can_with_complete_form(self):
        self.assertTrue(self.registration_form.is_valid)

    def test_both_passwords_entered(self):
        form = CustomUserCreationForm({
            'first_name': 'Lola',
            'last_name': 'Montez',
            'email': 'looloo@email.com',
            'username': 'looloo',
            'password1': '',
            'password2': 'yo!4password',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password1'],
                         ['This field is required.'])

    def test_username_is_unique_for_registration(self):
        self.assertTrue(self.registration_form.is_valid())
        self.registration_form.save()

        other_form = CustomUserCreationForm({
            'first_name': 'Lomax',
            'last_name': 'Montez',
            'email': 'lomax@email.com',
            'username': 'looloo',
            'password1': 'yo!4password',
            'password2': 'yo!4password',
        })

        self.assertFalse(other_form.is_valid())
        self.assertEqual(other_form.errors['username'],
                         ['A user with that username already exists.'])

                         
class TestProfileForm(TestCase):

    def test_profile_made_with_valid_form(self):
        form = ProfileForm({
            'first_name': 'Lola',
            'last_name': 'Montez',
            'email': 'looloo@email.com',
            'address_line_1': 'South Beach Street 99',
            'address_line_2': '',
            'postal_code': '23459RR',
        })
        self.assertTrue(form.is_valid())

    def test_profile_email_is_required(self):
        form = ProfileForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ProfileForm()
        self.assertEqual(form.Meta.fields,
                         ['first_name', 'last_name',
                          'email', 'address_line_1', 'address_line_2',
                          'postal_code', 'profile_image'])
                        
