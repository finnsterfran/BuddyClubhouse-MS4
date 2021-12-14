from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .widgets import CustomClearableFileInput
from django.core.exceptions import ValidationError
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    """ Form to create a new user """

    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'username', 'email', 'password1',
                  'password2']

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)


class ProfileForm(ModelForm):
    """ form to create profile or update profile """

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email',
                  'address_line_1', 'address_line_2', 'postal_code',
                  'profile_image']

    profile_image = forms.ImageField(label='Image',
                                     required=False,
                                     widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
