from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from .forms import CustomUserCreationForm, ProfileForm


def userLogin(request):
    """
    For user login, redirecting user to
    make an account if user doesn't exist in the database
    """
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.post['username']
        password = request.post['password']

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


def userLogout(request):
    """
    Log the user out
    """
    logout(request)
    messages.info(request, 'User is no longer logged in')
    return redirect('login')


def userRegister(request):
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


def profile(request, pk):
    """
    Display individual user profile
    """
    profile = Profile.objects.get(id=pk)

    context = {
        'profile': profile,
    }
    return render(request, 'users/profile.html', context)


@login_required(login_url='login')
def userAccount(request):
    """
    User's ACCOUNT view
    """
    profile = request.user.profile

    context = {
        'profile': profile
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
        form = ProfileForm(request, 'Profile update successful!')
        return redirect('account')

    context = {
        'form': form,
    }
    return render(request, 'users/profile_form.html', context)
