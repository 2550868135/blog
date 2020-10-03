$(function () {
    $(".click-li").mouseover(function (){
        $(this).addClass("active");
    })
     $(".click-li").mouseleave(function (){
        $(this).removeClass("active");
    })
    $(".click-li").click(function (){
        $(this).addClass("active");
    })

    function scrollConversationScreen() {
        $("textarea").focus();
        $('.content-main').scrollTop($('.content-main')[0].scrollHeight);
    }

    const ws_scheme = window.location.protocol === "https:" ? "wss" : "ws";
    //currentUser是在html中渲染时定义好的js变量,是登录的用户名
    const ws_path = ws_scheme + "://" + window.location.host  + "/ws/" + currentUser + "/";
	//建立连接
    const ws = new ReconnectingWebSocket(ws_path);

    //监听后端发送过来的数据
    ws.onmessage = function(event){
        const data = JSON.parse(event.data);       //把后端传来的JSON数据转为对象
        if(data.sender == activeUser){ //判断发送者为当前选中的用户
            $("#send-message").before(data.message); //将接收到的消息插入到聊天框
            scrollConversationScreen();  //执行滚动条下拉到底
            var csrf_token = $("input[name='csrfmiddlewaretoken']").val();
            $.ajax({
                url:'/blog/message/mark/',
                type: "POST",
                data:{
                    'sender':activeUser,
                    'csrfmiddlewaretoken':csrf_token
                }
            })
        }else{
            if(data.chat_item){
                $("#add-chat").before(data.chat_item);
                var base_chat = $("#chat-unread");
                if(!base_chat.hasClass("un-read")){
                    base_chat.addClass("un-read");
                }
            }else{
                var selecter = '#'+data.sender;
                var item = $(selecter).children(".unread");
                if(item.hasClass("come-unread")){
                    $("#"+data.sender).children(".unread").removeClass("come-unread");
                }
                var base_chat = $("#chat-unread");
                if(!base_chat.hasClass("un-read")){
                    base_chat.addClass("un-read");
                }
            }
        }
    };
});
