from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    User Profiles
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=300)
    postal_code = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to='profiles/',
                                      default='profiles/user-default.png')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.username)

    class Meta:
        ordering = ['created']
