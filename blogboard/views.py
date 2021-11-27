from django.shortcuts import render


def blogs(request):
    """
    View to see all the blogpost entries on the blogboard
    """
    return render(request, 'blogboard/blogs.html')