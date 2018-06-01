$(document).ready(function () {
});

$(document).on("click", "#register", function () {
    var username = $("#username").val();
    var password = $("#password").val();
    var name = $("#name").val();
    var id_number = $("#id-number").val();
    
    $.ajax({
        type:"post",
        url:"solve/",
        data:{
            "username":username,
            "password":password,
            "name":name,
            "id_number":id_number
        },

        success:function (data) {
            console.log(data);
            if (data == "1"){
                window.location.href = "../sports/pre_login"
            }
        }
    });
});