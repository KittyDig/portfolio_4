from django.urls import path
from . import views  # importing my views module

urlpatterns = [
    path('', views.home, name='home'),  # home page
    path('register/', views.register, name='register'),  # register page
]
