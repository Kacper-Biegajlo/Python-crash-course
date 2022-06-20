from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def index(request):
    """Homepage for blogs"""
    return render(request, 'blogs/index.html')

@login_required
def posts(request):
    """Shows the blogposts list"""
    posts = BlogPost.objects.order_by('date_added')
    context = {'posts': posts}
    return render(request, 'blogs/posts.html', context)

@login_required
def post(request, post_id):
    """Show a single blog post."""
    post = get_object_or_404(BlogPost, id=post_id)
    title = post.title
    text = post.text
    date = post.date_added
    owner = post.owner
    context = {'title': title, 'text': text, 'date': date, 'owner': owner}
    return render(request, 'blogs/post.html', context)

@login_required
def new_post(request):
    """Creating new topic"""
    if request.method != 'POST':
        #Data didn't sent; create empty form
        form = PostForm()
    else:
        # Data sent POST; process data
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:posts')

    # Show empty or invalid form
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    """Edit post"""
    post = get_object_or_404(BlogPost, id=post_id)
    check_post_owner(post.owner, request)
    
    if request.method != 'POST':
        # Request; form is filled with the data from current post
        form = PostForm(instance=post)

    else:
        # Sending POST data; process data
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:post', post_id=post.id)

    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)

def check_post_owner(owner, request):
    if owner != request.user:
        raise Http404