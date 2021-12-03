from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email',
                  'address_line_1', 'address_line_2',
                  'postal_code',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

