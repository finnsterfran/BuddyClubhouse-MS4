import uuid
from django.db import models


class Dog(models.Model):
    
    GENDER_TYPE = (
        ('Female', 'female'),
        ('Male', 'male'),
    )

    name = models.CharField(max_length=50)
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE, null=True)
    age = models.IntegerField()
    resided_since = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_TYPE)
    job = models.ManyToManyField('Job', blank=True)
    image = models.ImageField(upload_to='dogs/', null=True, blank=True)
    story = models.TextField(max_length=2000, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)
    
    class Meta: 
        ordering = ['resided_since']
    
    @property 
    def imageURL(self):
        try:
            url = self.image.url
        except AttributeError:
            url = ''
        return url


class Breed(models.Model):

    breed_name = models.CharField(max_length=20)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.breed_name)


class Job(models.Model):

    title = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.title)
