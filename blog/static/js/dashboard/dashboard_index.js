$(function (){


    //用户状态改变
    $("#update-status").click(function () {
        var url = $(this).attr('data-url');
        var able = $("#update-status input").val()
        if(able!=="1") {
            $.get(url, function (data) {
                if (data.code != 0) {
                    swal({
                        'title': '修改失败',
                        'button': '确定',
                        'type': "error"
                    });
                }
            });
        }
    });

});


