$(document).ready( function () {
    $('.input-daterange').datepicker({
        format: "yyyy 年 mm 月 dd 日",
        language: "zh-CN"
    });
} );
$(document).on("click", ".logout", function () {
    $.ajax({
        url: "../logout/",
        type: "post",
        async: false,
        success: function (response) {
            window.location.href="../login/"
        }
    });
});