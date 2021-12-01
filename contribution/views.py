from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from .models import Donation


def contribution(request):
    """ A view to show donation plans available """
    products = Donation.objects.all().order_by('price')
    context = {
        'products': products
    }
    return render(request, 'contribution/contribution.html', context)

