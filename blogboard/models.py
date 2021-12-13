from django.db import models
from users.models import Profile
from dogs.models import Dog


class Blog(models.Model):
    """
    Model for Blog database
    """
    title = models.CharField(max_length=200)
    username = models.ForeignKey(Profile, on_delete=models.CASCADE,
                                 null=True, blank=True)
    buddy_name = models.ForeignKey(Dog, on_delete=models.CASCADE,
                                   null=True)
    date_of_entry = models.DateTimeField(auto_now_add=True)
    featured_image = models.ImageField(upload_to='blogs/',
                                       null=True, blank=True)
    blog_entry = models.TextField(max_length=3000)

    def __str__(self):
        return str(self.title)
