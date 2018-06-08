$(document).on("click", ".logout", function () {
    $.ajax({
        url: "logout/",
        type: "post",
        async: false,
        success: function (response) {
            window.location.href="../login/"
        }
    });
});