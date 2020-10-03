$(function (){
   $(".publish-btn").click(function (event){
       event.preventDefault();
       var userId = $(".layui-form").attr('data-userid');
       var tag = $(".type").val();
       var title = $(".title").val();
       var real_content = $("textarea[name='content']").val();
       var show_content = $(".editormd-preview").text();
       var url = $(".layui-form").attr('data-url');
       var csrfToken = $("input[name='csrfmiddlewaretoken']").val();

       if(!title || !tag){
           swal({
                        'title': '标题或内容不能为空!',
                        'button': '确定',
                        'type': "error"
                        });
           return 1;
       }

       $.ajax({
           url:url,
           type:'post',
           data:{
               'user_id':userId,
               'tag':tag,
               'title':title,
               'real_content':real_content,
               'show_content':show_content,
               'csrfmiddlewaretoken':csrfToken
           },
           success:function (data){
                if(data.code == 0){
                    swal({
                        'title':data.message,
                        'showCancelButton': false,
                        'showConfirmButton': false,
                        'type': "success",
                        'timer':1000
                    },function(){
                        window.location.href = '/blog/index/all';
                    });

                }
                else{
                    swal({
                        'title': data.message,
                        'button': '确定',
                        'type': "error"
                        });
                }
           },
           fail: function(e){
               swal({
                        'title': '网络异常',
                        'button': '确定',
                        'type': "error"
                        });
           }
       })
   });
});