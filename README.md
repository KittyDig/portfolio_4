# My Django Project

This is a Django project that includes user authentication, profile management, and post management features. Users can create accounts, log in, edit their optional bio, create posts, view other user's accounts, and delete their posts with confirmation dialogs.

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
  - [CSS](#css)
  - [JS](#js)
- [Routes](#routes)
- [Sources](#sources)

## Motivation

The primary motivation for building this project was to create a personal blogging site where users can showcase their posts and share their thoughts through blog posts.

## Problem Solved

This project addresses the need for a simple yet functional platform where people can maintain a personal blog. It provides an easy-to-use interface for users to register, create and manage content, and interact with their own profile and others. This can be particularly useful for developers, designers, and other professionals who want to share updates or articles.

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
- **Viewing Other Profiles**: Users can click the usernames of other users to view their profiles.
- **Responsive Design**: Ensures the application is accessible on various devices.
- **Secure and Scalable**: Configured for secure authentication with passwords encrypted in the database and deployed on Heroku for scalability.


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
The custom user model inherits from AbstractUser to extend the default Django user functionality. This allows for future customization without modifying the built-in Django user model.

# Profile
The Profile model stores additional information about the user, such as a bio. It is linked to the User model via a one-to-one relationship.

# Post
The Post model stores user posts, including the title, content, and timestamp of creation. Each post is linked to an author, who is a user.

## Forms

# CustomUserCreationForm
Form for creating a new user.

# ProfileForm
Form for updating the user profile with additional information like a bio.

# PostForm
This form is used for creating and updating posts. It includes fields for the title and content of the post.

## Views

# Profile View
The profile view allows users to view and edit their profile. It displays the user's posts and optional bio, and includes a form for editing the bio.

# Post Management
The post management views include functions for creating, viewing, and deleting posts. Each view ensures that the user is logged in before they can perform these actions.

## Templates

# Profile Template
HTML template to display and edit the user profile.

## Static Files
Static files such as CSS, JS, and images are stored in the staticfiles directory.

# CSS
For the CSS in this project, I wanted it to have a sleek look, comparable to apps such as Instagram or Twitter. I wanted it to be mobile first design, so it looks good both on mobile devices and desktops.

# JS
The JavaScript in this project was not the main focus as this was a mainly Python built app, but it was used sparingly for moving from different pages.

# Routes
The routes for my application are defined in the urls.py file.

## Sources
# HTML files
- https://github.com/dev-bittu/djcms - Template referencing.
- https://github.com/dukeofhazardz/blog-app?tab=readme-ov-file#technologies - Help with both template structure and urls structure.
# CSS
- https://codepen.io/vladracoare/pen/YzEXveV - For inspiration for button type.
- https://coolors.co/ - For theme colour ideas.
# Views
- https://github.com/Akash1362000/Django_BlogApp - Help with understanding views.
- https://github.com/shivamforever/django-Codewithnc.py/ - Based structure of views on parts of this code.
- https://mentix02.medium.com/writing-instagram-in-python-liking-posts-51e072e4c51f - For help with liking posts code.
- https://www.atlassian.com/data/sql - For SQL help and understanding.
- https://stackoverflow.com/questions/29311354/how-to-set-the-timezone-in-django - For fixing a timezone problem.
# Models
- https://docs.djangoproject.com/en/5.0/topics/auth/customizing/ - Help with understanding custom models.
- https://stackoverflow.com/questions/75121950/how-to-use-authenticate-method-with-abstractuser-model-django help with the authentication model.
- https://medium.com/@engr.tanveersultan53/abstractuser-vs-abstractbaseuser-in-django-7f231a276988 - Finding information on abstractuser to see what authentication model to use.