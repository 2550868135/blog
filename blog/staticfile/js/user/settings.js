$(function (){
    //修改头像
    $("#head-btn").change(function upload(){
        var url = $(this).attr("data-url");
        var user = $(this).attr("data-user");
        var file = this.files[0];
        var csrfToken = $(this).prev().val();

        var formData=new FormData();
        formData.append("user",user);
        formData.append('file',file);
        formData.append('csrfmiddlewaretoken',csrfToken)
        $.ajax(
            {
                url:url,
                type: 'POST',
                contentType:false,
                processData:false,
                data:formData,
                success: function(data){
                    if(data.code == 0){
                        window.location.href = window.location.href
                    }
                    else{
                        swal({
                        'title': '修改失败',
                        'button': '确定',
                        'type': "error"
                        });
                    }
                },
                fail:function (){
                    swal({
                        'title': '网络异常',
                        'button': '确定',
                        'type': "error"
                        });
                }
            }
        )
     });

    var changeArea = $(".change");
    var staticArea = $(".static");

    //点击修改时弹出修改界面
    $(".update-settings").click(function (){
       var url = $(this).attr("data-url");
       staticArea.css("display","none");
       changeArea.css("display","block");
   });

    //点击重置按钮重置表单
    $(".reset-btn").click(function(){
        myForm = $(".setting-form");
        myForm[0].reset();
    })
});