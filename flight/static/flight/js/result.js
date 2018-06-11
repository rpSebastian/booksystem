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
    cond.leave_date = $("#leave-date").val();
    cond.leave_time = $(".leave-time" + id).html();
    swal({ 
        title: "确认订购该机票吗？", 
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
                success: function (data) {
                    if (data == '1')
                    {
                        swal({
                            title: "\n订购成功!", 
                            type: "success",
                        },
                        function(){
                            window.location.href="../check/"
                        });     
                    }
                    else
                    {
                        swal({
                            title: "\n该机票以售完\n请购买其他航班!", 
                            type: "error",
                        });                   
                    }
                }
            });
        }
      });
});

$(function() {
    $("#current1").text(2)
    $("#pagination1").pagination({
        currentPage: parseInt($("#pagecur").val()),
        totalPage: parseInt($("#pagetot").val()),
        callback: function(current) {
            $("#pagecur").val(current);
            $("#restart").val(2);
            $("#form").submit();
        }
    });

    $("#getPage").on("click", function() {
        var info = $("#pagination3").pagination("getPage");
        alert("当前页数：" + info.current + ",总页数：" + info.total);
    });

    $("#setPage").on("click", function() {
        $("#pagination3").pagination("setPage", 1, 10);
    });
});
