$(function (){
   $(".delete-btn").click(function (event){
        event.preventDefault();
        var data_id = $(this).parent().parent().attr('data-dataId');

        xtalert.alertConfirm({
            "msg": "您确定要删除这个资料吗?",
            'confirmCallback': function () {
                $.ajax({
                    url: '/blog/dashboard/data/delete/',
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