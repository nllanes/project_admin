/* Project specific Javascript goes here. */
var $document = $(document).ready(function(){
    signBtn = $('.sign-btn');


    function AjaxFormSubmit (form, context, bindToEnter, successCallback, errorCallback) {
            $.ajax({
                url: $(form).attr('action'),
                dataType: "html",
                type: $(form).attr('method'),
                data: $(form).serialize(),
                async: true,
                success: function(response) {
                    var responseHTML = $.parseHTML(response),
                        formResponse = $(responseHTML[1]).is('form') ?
                            $(responseHTML[1])
                            : $(responseHTML[1]).find('form');
                    if (formResponse && formResponse.find('.form-error').val() == 1) {
                        $(form).remove();
                        $(context).html(response);
                        if(errorCallback)
                            errorCallback();
                        $(context).find('.btn-accept').on('click', function(){
                            var form = $(this).parents('form');
                            AjaxFormSubmit(form, context, bindToEnter, successCallback, errorCallback);
                        });
                        if (bindToEnter) {
                            $(context).find('form').on('keypress', function (event) {
                                var keycode = (event.keyCode ? event.keyCode : event.which);
                                if(keycode == '13'){
                                    var form = $(this);
                                    AjaxFormSubmit(form, context, bindToEnter, successCallback, errorCallback);
                                }
                            });
                        }
                    }
                    else {
                        if(successCallback)
                            successCallback(response);
                    }

                },
                error: function(response) {
                    console.log(response);
                }
            });
        }

    // signBtn.on('click', function(){
    //         modalSignUp.find('.form-body').empty();
    //         $.ajax({
    //             url: $(this).data('ref'),
    //             dataType: "html",
    //             type: 'GET',
    //             async: true,
    //             success: function(response) {
    //                 modalSignUp.find('.form-body').append(response);
    //                 modalSignUp.find('.btn-accept').on('click', function(){
    //                     var form = $(this).parents('form'),
    //                         context = form.parents('.modal-body').find('.form-body');
    //                     AjaxFormSubmit(form, context, true, function (response) {
    //                         modalSignUp.modal('toggle');
    //                         modalSignUpSuccess.modal('toggle');
    //                     });
    //                 });
    //                 modalSignUp.find('form').on('keypress', function (event) {
    //                     var keycode = (event.keyCode ? event.keyCode : event.which);
    //                     if(keycode == '13'){
    //                         var form = $(this),
    //                         context = form.parents('.modal-body').find('.form-body');
    //                         AjaxFormSubmit(form, context, true, function (response) {
    //                             modalSignUp.modal('toggle');
    //                             modalSignUpSuccess.modal('toggle');
    //                         });
    //                     }
    //                 });
    //             },
    //             error: function(response) {
    //                 modalLogIn.find('.modal-body').append(response);
    //             }
    //         });
    //     });



    // using jQuery
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
});