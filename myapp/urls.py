from django.urls import path
from . import views  # importing views from the same directory
from django.contrib.auth import views as auth_views

app_name = 'myapp'  # specifying the application namespace

urlpatterns = [
    path('', views.home, name='home'),  # URL for the home page
    path('posts/', views.posts, name='posts'),  # URL for the posts page
    path('register/', views.register, name='register'),  # URL for the registration page
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # URL for the login page
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),  # URL for the logout page
    path('profile/', views.profile, name='profile'), # profile URL
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'), # URL for deleting posts from your own account
]
