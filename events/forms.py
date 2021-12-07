from django import forms
from .models import Event
from django.forms import ModelForm

class DateInput(forms.DateInput):
    input_type = 'date'

class EventForm(forms.ModelForm):
    
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
         'event_date': DateInput(),
        }

    def __init(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    