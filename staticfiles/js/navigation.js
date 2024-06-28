// JavaScript for navigating between pages
document.addEventListener('DOMContentLoaded', function() {
    // function to navigate from the home page to post page
    document.getElementById('goToPostPage').addEventListener('click', function() {
        window.location.href = '{% url "posts" %}';
    });

    // function to navigate from post page to home page
    document.getElementById('goToHomePage').addEventListener('click', function() {
        window.location.href = '{% url "home" %}';
    });
});
