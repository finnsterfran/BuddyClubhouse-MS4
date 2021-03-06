from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from blogboard.models import Blog
from checkout.models import Order
from .models import Profile
from .forms import CustomUserCreationForm, ProfileForm


def user_login(request):
    """
    For user login, redirecting user to
    make an account if user doesn't exist in the database
    """
    page = 'login'
    if request.user.is_authenticated:
        return redirect('account')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request,
                           'Username does not seem to exist in our database')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back {user}!')
            return redirect('account')
        else:
            messages.error(request,
                           'Uhm... username or/and password is incorrect!')
    return render(request, 'users/login_register.html')


def user_logout(request):
    """
    Log the user out
    """
    logout(request)
    messages.info(request, 'User is no longer logged in')
    return redirect('login')


def user_register(request):
    """
    For user registration page
    """
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():

            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'You have created a new user account')

            login(request, user,
                  backend='django.contrib.auth.backends.ModelBackend')
            return redirect('edit_account')
        else:
            messages.error(
                request, 'Sorry, something went wrong with the registration')
    context = {
        'page': page,
        'form': form,
    }
    return render(request, 'users/login_register.html', context)


def profiles(request):
    """
    Display all user profiles
    """
    profiles = Profile.objects.all()

    context = {
        'profiles': profiles
    }
    return render(request, 'users/profiles.html', context)


@login_required(login_url='login')
def user_account(request):
    """
    User's ACCOUNT view
    """
    profile = request.user.profile
    theBlogs = profile.blog_set.all()
    orders = profile.orders.all()

    context = {
        'profile': profile,
        'blogs': theBlogs,
        'orders': orders,
    }
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def edit_account(request):
    """
    User's ACCOUNT edit view, user can change profile
    and see all account related information
    """
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile update successful!')
            return redirect('account')

    context = {
        'form': form,
    }
    return render(request, 'users/profile_form.html', context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}.'
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_account': True,
    }
    return render(request, template, context)
