from django.db import models
from dogs.models import Dog


class Event(models.Model):
    title = models.CharField(max_length=200)
    event_type = models.OneToOneField('Event_Type', on_delete=models.CASCADE, null=True)
    buddy_name = models.ForeignKey(Dog, on_delete=models.CASCADE,
                                      null=True)
    date_of_event = models.DateField()
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return str(self.title)

class Event_Type(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)
