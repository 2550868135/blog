$(function (){
    $(".chat-item").mouseover(function (e){
        $(this).addClass('active')
    });
    $(".chat-item").mouseleave(function (e){
        $(this).removeClass("active")
    });

    function scrollConversationScreen() {
        $("textarea").focus();
        $('.content-main').scrollTop($('.content-main')[0].scrollHeight);
    }

    scrollConversationScreen();
    // const ws_scheme = window.location.protocol === "https:" ? "wss" : "ws";
    // //currentUser是在html中渲染时定义好的js变量,是登录的用户名
    // const ws_path = ws_scheme + "://" + window.location.host  + "/ws/" + currentUser + "/";
	// //建立连接
    // const ws = new ReconnectingWebSocket(ws_path);
    //
    // //监听后端发送过来的数据
    // ws.onmessage = function(event){
    //     const data = JSON.parse(event.data);       //把后端传来的JSON数据转为对象
    //     if(data.sender == activeUser){ //判断发送者为当前选中的用户
    //         $("#send-message").before(data.message); //将接收到的消息插入到聊天框
    //         scrollConversationScreen();  //执行滚动条下拉到底
    //     }else{
    //         if(data.chat_item){
    //             $("#add-chat").before(data.chat_item);
    //             var base_chat = $("#chat-unread");
    //             if(!base_chat.hasClass("un-read")){
    //                 base_chat.addClass("un-read");
    //             }
    //         }else{
    //             var selecter = '#'+data.sender;
    //             var item = $(selecter).children(".unread");
    //             if(item.hasClass("come-unread")){
    //                 $("#"+data.sender).children(".unread").removeClass("come-unread");
    //             }
    //             var base_chat = $("#chat-unread");
    //             if(!base_chat.hasClass("un-read")){
    //                 base_chat.addClass("un-read");
    //             }
    //         }
    //     }
    // };

    $("textarea").keydown(function (e){
        if(e.keyCode == 13){
            e.preventDefault();
            var content = $("textarea").val();
            if(!content || currentUser==activeUser){
                return;
            }
            var sender = currentUser;
            var recipient = activeUser;
            var csrf_token = $("input[name='csrfmiddlewaretoken']").val();
            $.ajax({
                url:'/blog/message/sendmessage/',
                type: "POST",
                data:{
                    'content':content,
                    'sender':sender,
                    'recipient':recipient,
                    'csrfmiddlewaretoken':csrf_token
                },
                success: function(data){
                    $("#send-message").before(data.message); //将接收到的消息插入到聊天框
                    $("textarea").val('');
                    scrollConversationScreen();  //执行滚动条下拉到底
                }
            })
        }
    })

});
