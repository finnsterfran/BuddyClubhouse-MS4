from django.test import TestCase
from .models import Blog


class TestModels(TestCase):
    def test_blog_str_method_returns_title(self):
        blog = Blog.objects.create(title='Test this')
        self.assertEqual(str(blog), 'Test this')
