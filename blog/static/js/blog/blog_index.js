$(function () {
    var flag = false;
    $(window).scroll(function () {
        if(flag){
            return false;
        }
        if ($(document).scrollTop() + $(window).height() + 1>= $(document).height()) {
            flag = true;
            var page = parseInt($(".article-show").attr('data-page'))+1;
            var totalPage = parseInt($(".article-show").attr('data-total-page'));
            if(page<= totalPage) {
                $.get(window.location.pathname+'?page='+page, function (data) {
                    jQuery.each(data.data, function (key, val) {
                        var div = $(".article-show");
                        var article_id = key;
                        var title = val.title;
                        var create_time = val.create_time;
                        var head_img = val.head_img;
                        var username = val.username;
                        var show_content = val.show_content;
                        var element = "<a href=\"/blog/detail/?id="+article_id+"\">\n" +
                            "        <div class=\"panel panel-info single-part\">\n" +
                            "            <div class=\"panel-heading\" style=\"position: relative\">\n" +
                            "                <h3 style=\"color: #0C1021;width: 50%;margin: 0\" ><p>"+title+"</p><span class=\"other\" style=\"position:absolute;right: 0;bottom:0;font-size: 14px\">"+create_time+"</span></h3>\n" +
                            "\n" +
                            "            </div>\n" +
                            "            <div class=\"panel-body\">\n" +
                            "                <p>\n" +
                            "                    <img src=\""+head_img+"\" alt=\"\" class=\"img-circle\" style=\"width: 30px;height:30px;display:  inline-block\"/>\n" +
                            "                    <span class=\"user-name\">"+username+ ": </span>\n" +
                            "                    <span class=\"other detail\">"+show_content+"</span>\n" +
                            "                </p>\n" +
                            "            </div>\n" +
                            "        </div>\n" +
                            "        </a>";
                        div.append(element);

                    });
                    $(".article-show").attr('data-page', page);
                    flag = false
                });
            }else{
                $("#is-bottom").css('display','block');
            }
        }
    });
});

// $(function () {
//     layui.use('flow', function () {
//         var $ = layui.jquery; //不用额外加载jQuery，flow模块本身是有依赖jQuery的，直接用即可。
//         var flow = layui.flow;
//         flow.load({
//             elem: '#demo' //指定列表容器
//             , done: function (page, next) { //到达临界点（默认滚动触发），触发下一页
//                 var lis = [];
//                 //以jQuery的Ajax请求为例，请求下一页数据（注意：page是从2开始返回）
//                 $.get('/api/list?page=' + page, function (res) {
//                     //假设你的列表返回在data集合中
//                     layui.each(res.data, function (index, item) {
//                         lis.push('<li>' + item.title + '</li>');
//                     });
//
//                     //执行下一页渲染，第二参数为：满足“加载更多”的条件，即后面仍有分页
//                     //pages为Ajax返回的总页数，只有当前页小于总页数的情况下，才会继续出现加载更多
//                     next(lis.join(''), page < res.pages);
//                 });
//             }
//         });
//     });
// });
