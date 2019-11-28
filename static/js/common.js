import 'https://polyfill.io/v3/polyfill.min.js';

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

let csrfToken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

const addCsrfToken = (xhr) => {
    xhr.setRequestHeader("X-CSRFToken", csrfToken);
};
/*
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain)
            xhr.setRequestHeader("X-CSRFToken", csrfToken);
    }
});*/

const movePage = (href) => location.href = href;

const stringToJson = (str) => {
    return eval("(" + str + ")");
};