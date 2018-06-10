$(document).ready(function () {

});
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
$(document).on("click", ".edit", function () {
    if (($(this).html()) == "编辑")
    {
        $(".display").hide();
        $(".update").show();
        $(".cancel").css("visibility","visible");
        $(this).html("保存");
    }
    else
    {
        var cond={};
        cond.name = $("#name").val();
        cond.id_number = $("#id-number").val();
        cond.phone_number = $("#phone-number").val();
        $.ajax({
            type: "post",
            url: "solve/",
            data: cond,
            success: function (response) {
                swal({
                    title: "\n保存成功!", 
                    type: "success",
                },
                function(){
                    window.location.href="../update/"
                });     
            }
        });
    }
});
$(document).on("click", ".cancel", function () {
    $(".display").show();
    $(".update").hide();
    $(".cancel").css("visibility","hidden");
    $(".edit").html("编辑");
});