// This file is used to load posts as the user scrolls down the page
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

$(document).ready(function () {
    let page = 1;

    function loadPosts() {
        $.ajax({
            url: "{% url 'update_feed' %}",
            data: {page: page},
            success: function (response) {
                let data = response.data;
                if (data === -1) {
                    return;
                }
                data.forEach(function (item) {
                    // Access item properties here and do whatever you need to do
                    console.log("Image URL:", item.image_url);
                    console.log("Username:", item.username);
                    console.log("Image ID:", item.image_id);
                    console.log("Page:", item.page);
                    let imageUrl = item.image_url;
                    let username = item.username;
                    let imageId = item.image_id;
                    let proilePicture = item.profile_picture_url;
                    // Example: Append the data to your HTML container
                    $('.feed').append('<div class="post"><div class="post-header"><img class="avatar" src="' + proilePicture + '" alt=""><span <a href="'+ "{% 'url'  %}" +'" class="username"> ' + username + ' </span></a> </div> <img src="' + imageUrl + '" alt="User Image"id=""> <div class="post-actions"></div><div class="post-caption"> <span class="username">Username:</span> <span class="caption-text">Caption text goes here...</span></div></div>');
                });
            }
        });
    }

    $(window).scroll(function () {
        if ($(window).scrollTop() + $(window).height() >= $(document).height() - 100) {
            loadPosts();
            page++;
        }
    });
    loadPosts(); // Load initial posts
});
