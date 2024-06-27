from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Post

# Handling user registration
def register(request):
    if request.method == 'POST':  # if the form has been submitted
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # saving the user to the database
            return redirect('login')
    else:  # if it's a GET request
        form = UserCreationForm()
    # renders the registration template with the form
    return render(request, 'register.html', {'form': form})

# Home page view
def home(request):
    posts = Post.objects.all()  # retrieves all posts from the database
    # renders the home template with all of the posts
    return render(request, 'home.html', {'posts': posts})

# Blog post detail view with login required
@login_required  # ensures the user is logged in to view this page
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})
