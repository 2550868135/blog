function f(){
    alert(10);
}
function upload(){
       alert(1);
        var url = $(".pic-manage").attr("data-url");
        var index = $(this).attr('data-index');
        var file = this.files[0];
        var csrfToken = $("input[name='csrfmiddlewaretoken']").val();
        alert(csrfToken);

        var formData=new FormData();
        formData.append('file',file);
        formData.append('index',index);
        formData.append('csrfmiddlewaretoken',csrfToken);
        $.ajax(
            {
                url:url,
                type: 'POST',
                contentType:false,
                processData:false,
                data:formData,
                success: function(data){
                    if(data.code == 0){
                        var image = data.image;
                        $(".insert-image:last").attr(src,image);
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
     }