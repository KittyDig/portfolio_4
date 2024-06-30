from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# custom User model inheriting from AbstractUser
class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Change the related_name
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',  # Change the related_name
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

# profile model to add more information to the User model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)  # bio, which is optional
    # profile picture, which is optional
    image = models.ImageField(upload_to='profile_pics', blank=True)

# post model to store blog posts
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)  # title for the post
    content = models.TextField()  # content of the post
    created_at = models.DateTimeField(auto_now_add=True)  # timestamp for post
