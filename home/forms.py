from django.forms import ModelForm
from .models import ContactUs


class ContactUsForm(ModelForm):
    """
    Form for users to get in touch with website admins/owners
    """
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'message']
