$(function (){
    $("#save-btn").click(function (event){
        event.preventDefault();
        var self = $(this);
        var dialog = $("#item-dialog");
        var describeInput = $("textarea[name='describe']");

        var describe = describeInput.val();
        var csrf = $("input[name='csrfmiddlewaretoken']").val();
        var file_url = $("input[name='file_url']").val();

        if(!describe || !file_url)
        {
            xtalert.alertInfoToast('请输入完整的项目信息!');
            return;
        }


        $.ajax({
            url:'/blog/datas/',
            type:'post',
            data:{
                'describe':describe,
                'file_url':file_url,
                'csrfmiddlewaretoken':csrf,
            },
            success: function(data){
                dialog.modal("hide");
                if(data.code == 0){
                    //重新加载页面
                    window.location.reload();
                }
                else{
                    xtalert.alertInfo(data.message);
                }
            },
            fail: function(e){
                xtalert.alertNetworkError();
            }
        })

    })
});
$(function (){
    $("#upload-btn").click(function () {
    var processGroup = $("#process-group");
    processGroup.css('display','block');
});
});