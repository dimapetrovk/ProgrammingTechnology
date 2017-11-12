$(document).ready(function () {
    $('#submit_delivery').click(function (e) {
        // Place new order
        var data = {
            is_delivered: document.getElementById("delivered_check").checked,
            car_is_broken: document.getElementById("car_is_broken_check").checked
        };
        $.ajax({
            method: 'PUT',
            data: JSON.stringify(data),
            url: '/api/order/' + window.location.pathname.split("/").slice(-1).pop(),
            headers: {
                'X-CSRFToken': document.cookie.split('=')[1],
                'Content-Type': 'application/json'
            }
        }).done(function (data) {
            window.location.pathname = '/';
        }).fail(function (err) {
            console.log(err);
        });
    });

    function login(data) {
        // Make login request
        $.ajax({
            url: '/login/',
            contentType: 'application/json',
            data: JSON.stringify(data),
            method: 'POST'
        }).done(function (res) {
            window.location.pathname = '/';
        }).fail(function () {
            alert('Wrong auth credentials');
        })
    }

    $('#sign_in_btn').click(function (e) {
        // Take values from inputs and login
        var data = {
            username: $('#sign_in_username_input').val(),
            password: $('#sign_in_password_input').val()
        };
        login(data);
    });

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});