from django.db import models

# create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models

# custom User model inheriting from AbstractUser


class User(AbstractUser):
    pass

# profile model to add to the User model with more information


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)  # bio, which is optional
    # profile picture, which is optional
    image = models.ImageField(upload_to='profile_pics', blank=True)

# post model to store blog posts or similar content


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)  # title for the post
    content = models.TextField()  # content of the post
    created_at = models.DateTimeField(auto_now_add=True)  # timestamp for post
