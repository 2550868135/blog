$(function () {
    $(".delete").click(function (event) {
        var self = $(this);
        var div = self.parent().parent().parent();
        var data_id = div.attr('data-dataId');
        event.preventDefault();

        xtalert.alertConfirm({
            "msg": "您确定要删除这个项目吗?",
            'confirmCallback': function () {
                $.ajax({
                    url: '/blog/mydata/deletedata/',
                    type: 'get',
                    data: {
                        'data_id': data_id
                    },
                    success: function (data) {
                        if (data.code == 0) {
                            window.location.reload();
                        } else {
                            xtalert.alertInfo(data.message);
                        }
                    },
                    fail: function (e) {
                        xtalert.alertNetworkError();
                    }
                });
            }
        });

    });

});

$(function () {
      $(".update").click(function (event){
          var self = $(this);
          var div = self.parent().parent().parent();

          var describe = div.attr('data-describe');
          var dataId = div.attr('data-dataId');


          $("textarea[name='describe']").val(describe);
          $("#save-btn").attr('data-dataId',dataId)

      })
});

$(function (){
    $("#save-btn").click(function (event){
        event.preventDefault();
        var self = $(this);
        var dialog = $("#item-dialog");
        var describeInput = $("textarea[name='describe']");

        var describe = describeInput.val();
        var csrf = $("input[name='csrfmiddlewaretoken']").val();
        var file_url = $("input[name='file_url']").val();
        var data_id = self.attr('data-dataId');

        if(!describe || !file_url)
        {
            xtalert.alertInfoToast('请输入完整的项目信息!');
            return;
        }


        $.ajax({
            url:'/blog/mydata/updatedata/',
            type:'post',
            data:{
                'describe':describe,
                'file_url':file_url,
                'csrfmiddlewaretoken':csrf,
                'data_id':data_id
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