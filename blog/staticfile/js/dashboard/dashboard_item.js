$(function (){
   $(".delete-btn").click(function (event){
        event.preventDefault();
        var item_id = $(this).parent().parent().attr('data-itemId');

        xtalert.alertConfirm({
            "msg": "您确定要删除这个项目吗?",
            'confirmCallback': function () {
                $.ajax({
                    url: '/blog/dashboard/item/delete/',
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