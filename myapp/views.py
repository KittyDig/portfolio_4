from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import User, Post, Profile
from .forms import CustomUserCreationForm, PostForm, ProfileForm 
from django.contrib.auth.decorators import login_required
from .models import Post

# Handling user registration
def register(request):
    if request.method == 'POST':  # if the form has been submitted
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # saving the user to the database
            return redirect('login')
    else:  # if it's a GET request
        form = CustomUserCreationForm()
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

# view for creating a new post
@login_required  # ensures the user is logged in to view this page
def posts(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('myapp:home')
    else:
        form = PostForm()
    return render(request, 'posts.html', {'form': form})

# view for the profile page
@login_required
def profile(request):
    user_posts = Post.objects.filter(author=request.user)
    context = {
        'user_posts': user_posts,
    }
    return render(request, 'accounts/profile.html', context)

# for deleting posts from the users page
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('myapp:profile')
    return render(request, 'confirmDeletePost.html', {'post': post})

# for making and updating the optional bio
def edit_bio(request):
    profile = Profile.objects.get_or_create(user=request.user)[0]

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('myapp:profile')
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'editBio.html', {'form': form})