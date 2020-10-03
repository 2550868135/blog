$(function (){
   if($(".single-part").length<=0){
       $(".article-no-post").show();
   }
   if ($(".item-d").length<=0){
       $(".item-no-post").show();
   }
   if ($(".data-d").length<=0){
       $(".data-no-post").show();
   }

   $('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
            switch($(e.target).attr("data-class")){
                case 'article':
                    var main=$(".single-part:last").offset().top+60;
                    var screens = document.body.clientHeight;
                    if(main>screens){
                        $(".block").height(main);
                    }else{
                        $(".block").height(screens);
                    }
                    break;
                case 'item':
                    var main=$(".single-item:last").offset().top+60;
                    var screens = document.body.clientHeight;
                    if(main>screens){
                        $(".block").height(main);
                    }else{
                        $(".block").height(screens);
                    }
                    break;
                case 'data':
                    var main=$(".single-item:last").offset().top+60;
                    var screens = document.body.clientHeight;
                    if(main>screens){
                        $(".block").height(main);
                    }else{
                        $(".block").height(screens);
                    }
                    break;
                default:
                    break;
            }
        });
});