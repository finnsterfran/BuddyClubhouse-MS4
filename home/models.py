from django.db import models


class ContactUs(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.TextField(max_length=500)
    contact_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
