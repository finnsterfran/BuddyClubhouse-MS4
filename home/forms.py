from django.forms import ModelForm
from .models import ContactUs

class ContactUsForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'

    def __init(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
