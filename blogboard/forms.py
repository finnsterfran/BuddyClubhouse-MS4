from django.forms import ModelForm
from .models import Blog

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = [
            'title',
            'buddy_name',
            'featured_image',
            'blog_entry',
        ]

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
