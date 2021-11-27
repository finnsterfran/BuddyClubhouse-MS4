from django.db import models
from users.models import Profile
from dogs.models import Dog 
import uuid


class Blog(models.Model):
    title = models.CharField(max_length=200)
    username = models.ForeignKey(Profile, on_delete=models.CASCADE,
                                 null=True, blank=True)
    name_of_buddy = models.ForeignKey(Dog, on_delete=models.CASCADE,
                                      null=True)
    date_of_entry = models.DateTimeField(auto_now_add=True)
    featured_image = models.ImageField(upload_to='blogs/',
                                       null=True, blank=True)
    blog_entry = models.TextField(max_length=3000, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.title)
