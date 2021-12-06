from django.shortcuts import render
from .models import Event


def events(request):
    all_events = Event.objects.all()
    context = {
        'all_events': all_events,
    }
    return render(request, 'events/events.html', context)


def single_event(request, pk):

    per_event = Event.objects.get(id=pk)
    context = {
        'per_event': per_event
    }
    return render(request, 'event/events.html', context)
