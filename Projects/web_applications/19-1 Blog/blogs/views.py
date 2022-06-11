from cgitb import text
from turtle import title
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse


from .models import BlogPost
from .forms import BlogPostForm

def index(request):
    """The home page for Blog."""
    return render(request, 'blogs/index.html')

def blogposts(request):
    """Show all blogposts."""
    blogposts = BlogPost.objects.order_by('date_added')
    context = {'blogposts': blogposts}
    return render(request, 'blogs/blogposts.html', context)

def blogpost(request, blogpost_id):
    """Show a single blog post."""
    topic = BlogPost.objects.get(id=blogpost_id)
    entries = topic.text
    date = topic.date_added
    context = {'title': topic, 'text': entries, 'date': date}
    return render(request, 'blogs/blogpost.html', context)

def new_blogpost(request):
    """Add a new blog post."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogPostForm()
    else:
        # POST data submitted; process data.
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogposts')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_blogpost.html', context)

def edit_blogpost(request, blogpost_id):
    '''Edit an existing post.'''

    entry = BlogPost.objects.get(id=blogpost_id)
    text = entry.text

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = BlogPostForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = BlogPostForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
    
    context = {'entry': entry, 'topic': text, 'form': form}
    return render(request, 'blogs/edit_blogpost.html', context)