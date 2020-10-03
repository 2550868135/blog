$(function (){
    $("#time").mouseenter(function (){
        var create = $(this).attr("data-create");
        var update = $(this).attr("data-update");
        var str = '最后发布:'+update+'<br/>首发:'+create;
        layer.tips(str,'#time', {tips: 3});
    });
    $("#time").mouseleave(function (){
        layer.closeAll();
    });
});

$(function(){
    $("#comment-btn").click(function(event){
        event.preventDefault();
        var csrf = $("input[name='csrfmiddlewaretoken']").val();
        var content = $("#comment-area").val();
        var article_id = $(".container").attr('data-articleId');

        if(!content){
            xtalert.alertInfoToast('请输入完整的项目信息!');
            return;
        }
        $.ajax({
            url:'/blog/detail/addcomment/',
            type:'post',
            data:{
                'csrfmiddlewaretoken':csrf,
                'content':content,
                'article_id':article_id
            },
            success:function (data){
                if (data.code == 0) {
                            window.location.reload();
                        } else {
                            xtalert.alertInfo(data.message);
                        }
            },
            fail: function (e){
                xtalert.alertNetworkError();
            }
        })
    });
});