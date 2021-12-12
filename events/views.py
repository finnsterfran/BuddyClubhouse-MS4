from django.shortcuts import render
from .models import Event


def events(request):
    """ View to render all events """
    all_events = Event.objects.all()
    context = {
        'all_events': all_events
    }
    return render(request, 'events/events.html', context)
