from django import forms
from django.forms import ModelForm
from .widgets import CustomClearableFileInput
from .models import Blog


class BlogForm(ModelForm):
    """
    Form for blog creation
    """
    class Meta:
        model = Blog
        fields = [
            'title',
            'buddy_name',
            'featured_image',
            'blog_entry',
        ]

    featured_image = forms.ImageField(label='Image',
                                      required=False,
                                      widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
