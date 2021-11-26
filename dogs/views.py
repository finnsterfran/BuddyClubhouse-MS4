from django.shortcuts import render
from .models import Dog


def dogs(request):
    """
    Display all dogs in the database
    """

    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        print('SEARCH:', search_query)

    
    dogs = Dog.objects.filter(name__icontains=search_query)

    context = {
        'dogs': dogs,
        'search_query': search_query
    }
    return render(request, 'dogs/dogs.html', context)


def dog_profile(request, pk):
    """
    display individual dog's profile
    """
    dogObj = Dog.objects.get(id=pk)

    context = {
        'dog_profile': dogObj,
    }
    return render(request, 'dogs/dog_profile.html', context)
