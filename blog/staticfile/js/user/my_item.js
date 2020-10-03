$(function () {
    $(".delete").click(function (event) {
        var self = $(this);
        var div = self.parent().parent().parent();
        var item_id = div.attr('data-itemId');
        var deleteUrl = div.attr('data-delete-url');
        event.preventDefault();

        xtalert.alertConfirm({
            "msg": "您确定要删除这个项目吗?",
            'confirmCallback': function () {
                $.ajax({
                    url: '/blog/myitem/deleteitem/',
                    type: 'get',
                    data: {
                        'item_id': item_id
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

          var introduce = div.attr('data-introduce');
          var name = div.attr('data-name');
          var itemId = div.attr('data-itemId');


          $("input[name='name']").val(name);
          $("textarea[name='introduce']").val(introduce);
          $("#save-btn").attr('data-itemId',itemId)

      })
});

$(function (){
    $("#save-btn").click(function (event){
        event.preventDefault();
        var self = $(this);
        var dialog = $("#item-dialog");
        var nameInput = $("input[name='name']");
        var introduceInput = $("textarea[name='introduce']");

        var name = nameInput.val();
        var introduce = introduceInput.val();
        var csrf = $("input[name='csrfmiddlewaretoken']").val();
        var file_url = $("input[name='file_url']").val();
        var item_id = self.attr('data-itemId');

        if(!name || !introduce || !file_url)
        {
            xtalert.alertInfoToast('请输入完整的项目信息!');
            return;
        }


        $.ajax({
            url:'/blog/myitem/updateitem/',
            type:'post',
            data:{
                'name':name,
                'introduce':introduce,
                'file_url':file_url,
                'csrfmiddlewaretoken':csrf,
                'item_id':item_id
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
