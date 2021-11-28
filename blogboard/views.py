from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Blog
from .forms import BlogForm


def blogs(request):
    """
    View to see all the blogpost entries on the blogboard
    """
    all_blogs = Blog.objects.all()
    context = {
        'all_blogs': all_blogs
    }
    return render(request, 'blogboard/blogs.html', context)


def blog_post(request, pk):
    """
    View to see individual blogpost entry on the blogboard
    """
    blogObj = Blog.objects.get(id=pk)
    context = {
        'blog_post': blogObj,
    }
    return render(request, 'blogboard/blog_post.html', context)


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
    }
    return render(request, 'blogboard/write_blog.html', context)


@login_required(login_url='login')
def edit_blog(request, pk):
    """
    View for user to edit their own existing blog post
    """
    profile = request.user.profile
    blog = profile.blog_set.get(id=pk)
    form = BlogForm(instance=blog)

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save()
            return redirect('blogs')

    context = {
        'blog': 'blog',
        'form': form,
    }
    return render(request, 'blogboard/write_blog.html', context)


@login_required(login_url='login')
def delete_blog(request, pk):
    """
    View to delete user's existing blog post
    """
    profile = request.user.profile
    blog = profile.blog_set.get(id=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('blogs')
    context = {
        'object': blog
    }
    return render(request, 'blogboard/delete_blog.html', context)
