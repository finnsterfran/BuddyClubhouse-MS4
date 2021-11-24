from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }

        def __init__(self, *args, *kwargs):
            super(CustomUserCreationForm, self).__init__(*args, **kwargs)


class ProfileForm(ModelForm):
    class Meta: 
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'contact_number', 'profile_image']

    def __init__(self, *args, *kwargs):
        super(ProfileForm, self).__init__(*args, *kwargs)
