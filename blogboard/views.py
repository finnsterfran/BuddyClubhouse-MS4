from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Blog
from .forms import BlogForm


def blogs(request):
    """
    View to see all the blogpost entries on the blogboard
    """
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blogboard/blogs.html', context)




@login_required(login_url='login')
def write_blog(request):
    """
    View to create and submit a new blog post entry
    """
    profile = request.user.profile
    form = BlogForm()

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.username = profile
            blog.save()

            messages.success(request, 'You have submitted a new blog entry!')
            return redirect('blogs')

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'blogboard/write_blog.html', context)
