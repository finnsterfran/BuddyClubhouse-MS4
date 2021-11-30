from django.shortcuts import render


def contribution(request):
    """ A view to show donation plans available """
    return render(request, 'contribution/contribution.html')

