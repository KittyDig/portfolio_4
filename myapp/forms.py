# myapp/forms.py

from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from myapp.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']