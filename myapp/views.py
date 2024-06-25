from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Post

# for handling user registration


def register(request):
    if request.method == 'POST':  # if the form has been submitted
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # saving the user to the database
            return redirect('login')
    else:  # if its a GET request
        form = UserCreationForm()
    # renders the registration template with the form
    return render(request, 'register.html', {'form': form})


@login_required  # ensures the user is logged in to view this page
def home(request):
    posts = Post.objects.all()  # retrieves all posts from the database
    # renders the home template with all of the posts
    return render(request, 'home.html', {'posts': posts})
