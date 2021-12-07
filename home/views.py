from django.shortcuts import render, redirect
from .forms import ContactUsForm
from django.contrib import messages


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


def contact_us(request):
    """
    A view to render contact_us form
    """
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message.'
                             'We will get in touch soon.')
            return redirect('home')
    form = ContactUsForm()
    context = {'form': form}
    return render(request, 'home/contact_us.html', context)
