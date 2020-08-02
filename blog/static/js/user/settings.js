$(function (){
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
                        alert('修改成功');
                        window.location.href = window.location.href
                    }
                    else{
                        alert('修改失败')
                    }
                },
                fail:function (){
                    alert('修改失败!')
                }
            }
        )
     });

    var changeArea = $(".change");
    var staticArea = $(".static");

    $(".update-settings").click(function (){
       var url = $(this).attr("data-url");
       staticArea.css("display","none");
       changeArea.css("display","block");
   })
});