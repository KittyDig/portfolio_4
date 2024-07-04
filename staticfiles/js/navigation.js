// JavaScript for navigating between pages
//function to go from homepage to posts page
document.addEventListener('DOMContentLoaded', function() {
    var goToPostPageButton = document.getElementById('goToPostPage');
    if (goToPostPageButton) {
        goToPostPageButton.addEventListener('click', function() {
            window.location.href = postsUrl;
        });
    }

    //function to go from posts page to home page
    var goToHomePageButton = document.getElementById('goToHomePage');
    if (goToHomePageButton) {
        goToHomePageButton.addEventListener('click', function() {
            window.location.href = home;
        });
    }
});

