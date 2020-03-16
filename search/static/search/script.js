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

// overwrite modal open functionality
// clear the message if one exists
if ($('#send-message-modal').length > 0)
{
    $('#send-message-modal').click((e) => {
        e.preventDefault();
        ClearModal();
        $('#contact-prof-modal').modal('show');
    })
}

function ClearModal() {
    $('#contact-prof-result-message').hide();
    $('.form-group .form-control').val('');
    ClearModalErrors();
};

function ClearModalErrors() {
    $('.modal-error').html('');
    $('#contact-prof-result-message').removeClass();
}

// Make AJAX request to send email to wellness professional
if ($('#contact-form-submit').length > 0)
{
    var csrfToken = getCookie('csrftoken');
    
    $('#contact-form-submit').click((e) => {
        e.preventDefault();
        var contactForm = $("#contact-form");
        $.ajax({
            beforeSend: function(xhr) {
                if (!this.crossdomain) {
                    xhr.setRequestHeader('X-CSRFToken', csrfToken);
                }
            },
            method: "POST",
            url: contactForm.attr('action'),
            data: contactForm.serialize(),
            success: function (response) {
                if (response['success'])
                {
                    ClearModalErrors();
                    $('#contact-prof-modal').modal('hide');
                    $('#contact-prof-success-message').addClass('alert alert-success fade show');
                    $('#contact-prof-success-message').html('Message Sent! <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>');
                }
                else if (response['error'])
                {
                    ClearModalErrors();
                    $('#contact-prof-result-message').addClass('alert alert-danger fade show');
                    $('#contact-prof-result-message').html('Oops! We encountered an error!');
                    $('#contact-prof-result-message').show();
                    
                    for (var field in response['error'])
                    {
                        $('#error-' + field).html(response['error'][field]);  
                    }
                                     
                }
            },
            error: function (response) {
                //console.log('FAILURE: ' + JSON.stringify(response));
                $('#contact-form').html(response.responseText);
            }
        });
    })
};

// check to make sure passwords match on sign up page
if($("#id_password, #id_retype_password").length > 0)
{

    $("#id_password, #id_retype_password").keyup(function (e) {
        var password = $("#id_password").val();
        var password2 = $("#id_retype_password").val();
        if (password != password2)
        {
            $("#id_retype_password").css('background-color','lightpink');
            $("#btnSearch").prop("disabled",true);
        }
        else if ((password != "" && password2 != "") && (password == password2))
        {
            $("#id_retype_password").css('background-color','lightgreen');
            $("#btnSearch").prop("disabled",false);
        }
        else if (password == "" && password2 == "") {
            $("#id_retype_password").css('background-color','white');
            $("#btnSearch").prop("disabled",false);
        }
    });
}