# myapp/forms.py

from django import forms
from .models import Post
from myapp.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']