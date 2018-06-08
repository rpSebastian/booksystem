
$(document).on("click", "#login", function () {
    var username = $("#username").val();
    var password = $("#password").val();
    $.ajax({
        type:"post",
        url:"solve/",
        data:{
            'username':username,
            'password':password
        },
        success:function (data) {
            console.log(data);
            if (data == "1"){
                swal({
                    title: "\n登陆成功!",
                    text: "",
                    type: "success",
                    confirmButtonText: "OK"
                },
                function () {
                    window.location.href = "../index/"
                });
            }
            if(data == "2"){
                console.log("ggsmd")
                swal({
                    title: "\n用户名或密码错误!",
                    text: "",
                    type: "error",
                    confirmButtonText: "OK"
                });
            }
        }
    });
});
