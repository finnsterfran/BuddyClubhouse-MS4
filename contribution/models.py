from django.db import models
from django.contrib.auth.models import User


class Donation(models.Model):
    """
    Model for choices of donation that user can make
    """
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    short_info = models.CharField(max_length=255, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
