from django.shortcuts import render

# Create your views here.
def dogs(request):
    """
    display all dogs in the database
    """
    dogs = Dog.objects.all()

    context = {
        'dogs': dogs,
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
