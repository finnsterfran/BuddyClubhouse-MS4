import uuid
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    """
    User Profiles
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=300)
    postal_code = models.CharField(max_length=20)
    contact_number = models.IntegerField()
    profile_image = models.ImageField(upload_to='profiles/', default='profiles/user-default.png')
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.user.username)

    class Meta:
        ordering = ['created']
