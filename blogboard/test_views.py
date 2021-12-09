from django.test import TestCase
from .models import Blog
from django.contrib.auth.models import User
from . import views


class TestViews(TestCase):
    def setUp(self):
        test_user = User.objects.create_user(username='looloo', password='yo!4password')
        test_user.save()
        
    def test_get_blogs(self):
        response = self.client.get('/blogboard/') 
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogboard/blogs.html')

    def test_get_write_blog_page(self):
        login_okay = self.client.login(username='looloo', password="yo!4password")
        self.assertTrue(login_okay)
        response = self.client.get('/blogboard/write_blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogboard/write_blog.html')

    def test_can_add_blog(self):
        login_okay = self.client.login(username='looloo', password="yo!4password") 
        self.assertTrue(login_okay)
        response = self.client.post('/blogboard/write_blog/', {'title': 'Test add a blog'})
        self.assertTemplateUsed(response, 'blogboard/write_blog.html')
