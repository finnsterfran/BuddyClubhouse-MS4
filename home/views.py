from django.shortcuts import render


def index(request):
    """
    A view to return the HOME page
    """
    return render(request, 'home/index.html')


def about(request):
    """
    A view to render the ABOUT page
    """
    return render(request, 'home/about.html')
