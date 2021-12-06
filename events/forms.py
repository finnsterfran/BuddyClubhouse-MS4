from django import forms
from .models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'
    
    def __init(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    