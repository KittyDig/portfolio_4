# My Django Project

This is a Django project that includes user authentication, profile management, and post management features. Users can create accounts, log in, edit their profiles, create posts, and delete their posts with confirmation dialogs.

## Table of Contents

- [Motivation](#motivation)
- [Problem Solved](#problem-solved)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Models](#models)
  - [User](#user)
  - [Profile](#profile)
  - [Post](#post)
- [Forms](#forms)
  - [CustomUserCreationForm](#customusercreationform)
  - [ProfileForm](#profileform)
  - [PostForm](#postform)
- [Views](#views)
  - [Profile View](#profile-view)
  - [Post Management](#post-management)
- [Templates](#templates)
  - [Profile Template](#profile-template)
- [Static Files](#static-files)
- [Routes](#routes)

## Motivation

The primary motivation for building this project was to create a personal blogging site where users can showcase their posts and share their thoughts through blog posts.

## Problem Solved

This project addresses the need for a simple yet functional platform where individuals can maintain a personal blog. It provides an easy-to-use interface for users to register, create and manage content, and interact with their profiles. This can be particularly useful for developers, designers, and other professionals who want to share updates or articles.

## Technologies Used

- **Django**
- **PostgreSQL**
- **Django-Heroku**
- **HTML/CSS**

## Features

- **User Registration and Authentication**: Allows users to create accounts, log in, and log out.
- **Custom User Model**: Uses a custom user model to extend the default Django user functionality.
- **User Profile Management**: Users can edit their bio.
- **Blog Post Management**: Users can create, read, update, and delete blog posts.
- **Responsive Design**: Ensures the application is accessible on various devices.
- **Secure and Scalable**: Configured for secure authentication and deployed on Heroku for scalability.


## Installation

To install this project, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject

2. Create a virtual environment and activate it:
    ```bash
   python -m venv env
   source env/bin/activate

3. Install the required packages:
    ```bash
   pip install -r requirements.txt

4. Apply the migrations:
    ```bash
   python manage.py makemigrations
   python manage.py migrate

5. Create a superuser to access the admin panel:
    ```bash
   python manage.py createsuperuser

6. Run the development server:
    ```bash
    python manage.py runserver

## Configuration
Ensure you have configured your settings.py file correctly, especially for DATABASES, INSTALLED_APPS, and MEDIA_URL/MEDIA_ROOT.

## Usage
1. Access the admin panel at http://127.0.0.1:8000/admin and log in with your superuser credentials.
2. Create, view, and manage user profiles and posts from the admin panel or through the provided forms and views.

## Project Structure
portfolio_4/
├── myapp/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── staticfiles/
├── manage.py
└── requirements.txt

## Models

# User
Custom user model inheriting from AbstractUser.

# Profile
Model to store additional information about the user, such as a bio and profile picture.

# Post
Model to store user posts with title and content.

## Forms

# CustomUserCreationForm
Form for creating a new user.

# ProfileForm
Form for updating the user profile with additional information like a bio.

# PostForm
Form for creating and updating posts.

## Views

# Profile View
Allows users to view and edit their profile.

# Post Management
Allows users to create, view, and delete their posts.

## Templates

# Profile Template
HTML template to display and edit the user profile.

## Static Files
Static files such as CSS and images are stored in the staticfiles directory.

# Routes
The routes for my application are defined in the urls.py file.