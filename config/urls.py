"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import include, path

# defines the URL patterns for the whole project
urlpatterns = [
    path('admin/', admin.site.urls),  # URL for the admin interface
    path('', include('myapp.urls')),  # includes URLs from the application
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # login URL pattern
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # logout URL pattern
    path('accounts/', include('accounts.urls')),  # Include accounts URLs
]
