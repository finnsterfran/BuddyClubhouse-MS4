from django.test import TestCase
from .models import Event, Event_Type


class Testmodels(TestCase):
    def test_event_str_method_returns_title(self):
        event = Event.objects.create(title='Ballpark', 
                                     date_of_event='2021-12-12',
                                     start_time='09:00', 
                                     end_time='11:00')
        self.assertEqual(str(event), 'Ballpark')
    
    def test_eventtype_str_method_returns_name(self):
        eventtype = Event_Type.objects.create(name='playdate')
        self.assertEqual(str(eventtype), 'playdate')
