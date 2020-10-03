$(function (){

    //添加图片项目
   $(".add-pic").click(function (){
       var picItem = `<div class=\"col-sm-6 col-md-4 count-image\"><div class=\"thumbnail\"><img class='insert-image' src='' alt='未选择图片' style=\"height:250px;\"><div class=\"caption\"><p style=\"position: relative;width: 100%\"><a href=\"\" class=\"btn btn-primary\" role=\"button\" style=\"margin: 0 3%\">选择图片</a><input type=\"file\" class=\"select-pic-btn\" style=\"position: absolute;opacity: 0;left: 0px;top: 0px;width: 50%;\" accept=\"image/*\" onchange=\"upload(this)\"><a href=\"\" class=\"btn btn-primary delete-btn\" role=\"button\" style=\"margin: 0 3%;position: absolute;right: 0;\" onclick=\"delPic(this)\">删除</a></p></div></div></div>`;
       $(".add-item").before(picItem);
   });


});

function upload(that){
        // var index = parseInt($(that).attr('data-index'));
        var index = $(".select-pic-btn").index(that)+1;
        var fileBtn = $(that);
        var url = $(".pic-manage").attr("data-url");
        var file = fileBtn[0].files[0];
        var csrfToken = $("input[name=\"csrfmiddlewaretoken\"]").val();


        var formData=new FormData();
        formData.set('file',file);
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
                        // $(".insert-image:last").attr('src',image);
                        window.location.reload();
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

function delPic(that) {
    var index = $(that).attr('data-index');
    // var index = $(".delete-btn").index(that)+1;
    var url = $(".pic-manage").attr("data-remove");
    $.ajax({
        url:url,
        type:'get',
        data:{
            'index':index
        },
        success:function(data){
            if(data.code == 0){
                var parents = $(that).parentsUntil("div.panel-body");
                parents.remove();
                that.remove();
            }
            else {
                swal({
                        'title': data.message,
                        'button': '确定',
                        'type': "error"
                        });
            }
        },
        fail:function (e) {
            swal({
                        'title': '网络异常',
                        'button': '确定',
                        'type': "error"
                    });
        }
    });
}