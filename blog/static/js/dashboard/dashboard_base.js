$(function (){
    //侧导航栏高亮选中
        var url = window.location.href;
        if(url.indexOf('user') >= 0)
        {
            $(".avail-item").removeClass('active');
            $(".avail-item").eq(0).addClass('active')
        }
        else if(url.indexOf('picture') >= 0) {
            $(".avail-item").removeClass('active');
            $(".avail-item").eq(4).addClass('active')
        }
});