from django.test import TestCase
from .forms import ProfileForm

class TestProfileForm(TestCase):

    def test_profile_email_is_required(self):
        form = ProfileForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ProfileForm()
        self.assertEqual(form.Meta.fields, ['first_name', 'last_name', 'email', 'address', 'postal_code', 'contact_number', 'profile_image'])
