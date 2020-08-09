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
});
