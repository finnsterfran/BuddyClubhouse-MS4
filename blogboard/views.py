from django.shortcuts import render, redirect, get_object_or_404
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


def blog_entry(request, pk):
    """
    View to see individual blogpost entry on the blogboard
    """
    
    blogpost = Blog.objects.get(id=pk)
    context = {
        'blogpost': blogpost,
    }
    return render(request, 'blogboard/blog_entry.html', context)


@login_required()
def write_blog(request):
    """
    View to create and submit a new blog post entry
    """
    profile = request.user.profile
    form = BlogForm()

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.username = profile
            blogpost.save()

            messages.success(request, 'You have submitted a new blog entry!')
            return redirect('blogs')

    context = {
        'form': form,
    }
    return render(request, 'blogboard/write_blog.html', context)


@login_required
def edit_blog(request, pk):
    profile = request.user.profile
    blogpost = profile.blog_set.get(id=pk)
    form = BlogForm(instance=blogpost)

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blogpost)
        if form.is_valid():
            blogpost = form.save()
            messages.success(request, 'Blog updated')
            return redirect('blogs')
    context = {
        'form': form,
        'blogpost': blogpost,
    }
    return render(request, 'blogboard/write_blog.html', context)


@login_required
def delete_blog(request, pk):
    profile = request.user.profile
    blogpost = profile.blog_set.get(id=pk)
    if request.method == 'POST':
        blogpost.delete()
        messages.success(request, 'Blog post deleted')
        return redirect('blogs')
    context = {
        'blogpost': blogpost
    }
    return render(request, 'blogboard/delete_blog.html', context)
