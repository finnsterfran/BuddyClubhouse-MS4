from django.db import models
from dogs.models import Dog


class Event(models.Model):
    """ Model for Events Details """

    EVENT_TYPE = (
        ('PLAYDATE', 'playdate'),
        ('MUSHING/SKIJORING TRAINING', 'musher-training'),
        ('WATER TRAINING', 'water-training'),
        ('AGILITY TRAINING', 'agility-training'),
        ('OTHER TRAINING', 'other-training'),
        ('OPEN DAY', 'open-day-playdate'),
        ('VOLUNTEER DAY', 'volunteer-day'),
        ('HIKE', 'hike')
    )
    TIME_SLOT = (
        ('PLAYDATE MORNING', '09:00 - 11:00'),
        ('PLAYDATE AFTERNOON', '13:00 - 15:00'),
        ('OPEN DAY PLAYDATE', '10:00 - 16:00'),
        ('TRAINING 1', '08:00 - 10:00'),
        ('TRAINING 2', '10:00 - 12:00'),
        ('HIKE 1', '09:00 - 12:00'),
        ('HIKE 2', '13:00 - 16:00'),
        ('VOLUNTEER DAY', '09:00 - 16:00'),
    )
    title = models.CharField(max_length=200, null=False, blank=False)
    name_of_buddy = models.ForeignKey(Dog, on_delete=models.SET_NULL,
                                      null=True)
    activity = models.CharField(max_length=100, choices=EVENT_TYPE)
    time_block = models.CharField(max_length=30, choices=TIME_SLOT)
    event_date = models.DateField()
    description = models.CharField(max_length=1000, null=True, blank=True)
    available = models.BooleanField(null=False, blank=False, default=True)

    def __str__(self):
        return str(self.title)
