from django.urls import path
from . import views  # importing my views module

urlpatterns = [
    path('', views.home, name='home'),  # home page
    path('register/', views.register, name='register'),  # register page
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),
         name='login'),  # login page
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'),
         name='logout'),  # logout page

]
