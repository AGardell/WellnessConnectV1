// for ajax calls, obtain the crsf token by looping through cookies
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Live Well, Connect Well fade
$(document).ready(() => {
    $("#span-connect").fadeTo(1000, 1);
    $("#span-live").delay(1000).fadeTo(1000, 1);
});

// Display search bar in header if user is not on search page
if ($('#navbar-main').length > 0)
{
    $('#navbar-search').hide();
}
else if ($('navbar-search').is(':hidden')) {
    $('$navbar-search').show();
}

// Make AJAX request to send email to wellness professional
if ($('#contact-form-submit').length > 0)
{
    var csrfToken = getCookie('csrftoken');
    
    $('#contact-form-submit').click((e) => {
        e.preventDefault();
        var contactForm = $("#contact-form");
        //var contactForm = $("#contact-form")[0];
        //var fd = new FormData(contactForm)
        $.ajax({
            beforeSend: function(xhr) {
                if (!this.crossdomain) {
                    xhr.setRequestHeader('X-CSRFToken', csrfToken);
                    //alert('Token set!');
                }
            },
            method: "POST",
            url: contactForm.attr('action'),
            data: contactForm.serialize(),
            //data: fd,
            success: function (response) {
                $("#contact-prof-modal").modal('hide');
                //alert(JSON.stringify(response));
                alert('SUCCESS: ' + response.responseText);
            },
            error: function (response) {
                //alert(JSON.stringify(response));
                console.log('FAILURE: ' + JSON.stringify(response));
                $('#contact-form').html(response.responseText);
            }
        });
    })
};