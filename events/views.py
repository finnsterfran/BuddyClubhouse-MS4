from django.shortcuts import (render, redirect,
                              reverse, get_object_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm


def events(request):
    """
    Display all existing events
    """
    all_events = Event.objects.all()
    context = {
        'all_events': all_events,
    }
    return render(request, 'events/events.html', context)


def single_event(request, event_id):
    """
    Display single existing events
    """
    event = Event.objects.get(pk=event_id)
    context = {
        'object': event
    }
    return render(request, 'events/single_event.html', context)


@login_required
def add_event(request):
    """
    Add a new event
    """
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            messages.success(request, 'New event has been added!')
            return redirect(reverse('single_event', args=[event.id]))
        else:
            messages.error(request, 'Could not add event.'
                           'Please double check the details.')
    else:
        form = EventForm()

    context = {
        'form': form,
    }
    return render(request, 'events/add_event.html', context)


@login_required
def edit_event(request, event_id):
    """
    Edit an existing event
    """
    event = get_object_or_404(Event, pk=event_id)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event has been updated!')
            return redirect(reverse('single_event', args=[event.id]))
        else:
            messages.error(request, 'Cannot update this event.'
                           'Check the form for mistakes.')
    else:
        form = EventForm(instance=event)
        messages.info(request, f'You are editing {event.title}')

    context = {
        'form': form,
        'event': event,
    }
    return render(request, 'events/edit_event.html', context)


@login_required
def delete_event(request, event_id):
    """
    Delete an event
    """
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted')
        return redirect('events')
    context = {
        'event': event,
    }
    return render(request, 'events/delete_event.html', context)
