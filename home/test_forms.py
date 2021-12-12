from django.test import TestCase
from .forms import ContactUsForm


class TestContactUsForm(TestCase):

    def test_create_contactus_form_with_required_fields_filled(self):
        form = ContactUsForm({
            'name': 'Lomax Manning',
            'email': 'lomanning@email.com',
            'message': 'some sort of message about something',
        })
        self.assertTrue(form.is_valid())
