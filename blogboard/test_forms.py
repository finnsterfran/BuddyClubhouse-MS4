from django.test import TestCase
from .forms import BlogForm

class TestBlogForm(TestCase):

    def test_form_can_be_submitted_without_title(self):
        form = BlogForm({
            'title': '',
            'buddy_name': 'Daisy',
            'blog_entry': 'a bunch of text'
            })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'][0], 'This field is required.')
    
    def test_form_can_be_submitted_without_title(self):
        form = BlogForm({
            'title': '',
            'buddy_name': 'Daisy',
            'blog_entry': 'a bunch of text'
            })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'][0], 'This field is required.')
    
    def test_form_can_be_submitted_without_buddy_name(self):
        form = BlogForm({
            'title': 'a blog',
            'buddy_name': '',
            'blog_entry': 'a bunch of text'
            })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['buddy_name'][0], 'This field is required.')

    def test_form_can_be_submitted_without_blog_entry(self):
        form = BlogForm({
            'title': 'a blog',
            'buddy_name': 'Daisy',
            'blog_entry': ''
            })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['blog_entry'][0], 'This field is required.')
