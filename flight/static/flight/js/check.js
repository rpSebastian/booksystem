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
$(document).on("click", "#search", function () {
    var cond={};
    cond.leave_city = $("#leave-city").val();
    cond.arrive_city = $("#arrive-city").val();
    cond.leave_date = $("#leave-date").val();
    cond.arrive_date = $("#arrive-date").val(); 
});
$(document).on("click", ".booking", function () {
    var cond={};
    var id = $(this).attr("id").substring(7);
    cond.flight_id = $("#flight-id" + id).html();
    cond.leave_time = $(".leave_time" + id).html();
    swal({ 
        title: "确认取消订购该机票吗？", 
        type: "warning",
        showCancelButton: true, 
        animation: "slide-from-top", 
        confirmButtonColor: "#DD6B55",
        confirmButtonText: "当然了！", 
        cancelButtonText: "点错啦！",
        closeOnConfirm: false, 
        closeOnCancel: true	
      },
      function(isConfirm){ 
        if (isConfirm) { 
            $.ajax({
                type: "post",
                url: "booking/",
                data: cond,
                success: function (response) {
                    swal({
                        title: "\n取消成功!", 
                        type: "success",
                    },
                    function(){
                        window.location.href="../check/"
                    });     
                }
            });
        }
      });
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