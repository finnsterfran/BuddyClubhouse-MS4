from django.db import models
from dogs.models import Dog


class Event(models.Model):
    """ Model for Events Details """

    EVENT_TYPE = (
        ('PLAYDATE', 'playdate'),
        ('WATER_TRAINING', 'train-water'),
        ('AGILITY_TRAINING', 'train-agility'),
        ('HIKE', 'hike')
    )
    TIME_SLOT = (
        ('PLAYDATE_MORNING', '09:00 - 11:00'),
        ('PLAYDATE_AFTERNOON', '13:00 - 15:00'),
        ('TRAINING', '08:00 - 10:00'),
        ('HIKE', '13:00 - 16:00'),
    )
    title = models.CharField(max_length=200, null=False, blank=False)
    name_of_buddy = models.ForeignKey(Dog, on_delete=models.SET_NULL,
                                      null=True)
    activity = models.CharField(max_length= 100, choices=EVENT_TYPE)
    time_block = models.CharField(max_length=30, choices=TIME_SLOT)
    date = models.DateField()
    available = models.BooleanField(null=False, blank=False, default=True)

    def __str__(self):
        return str(self.title)
