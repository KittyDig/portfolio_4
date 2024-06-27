from django.urls import path
from . import views  # importing views from the same directory
from django.contrib.auth import views as auth_views

app_name = 'myapp'  # specifying the application namespace

urlpatterns = [
    path('', views.home, name='home'),  # URL for the home page
    path('register/', views.register, name='register'),  # URL for the registration page
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # URL for the login page
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),  # URL for the logout page
]
