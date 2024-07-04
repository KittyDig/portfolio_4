from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# custom User model inheriting from AbstractUser
class User(AbstractUser):
    pass

# profile model to add more information to the User model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)  # bio, which is optional
    # profile picture, which is optional
    image = models.ImageField(upload_to='profile_pics', blank=True)

# post model to store blog posts
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='post_likes')

    def total_likes(self):
        return self.likes.count()