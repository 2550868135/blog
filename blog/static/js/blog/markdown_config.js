 var testEditor = editormd("editormd", {
    width: "100%",
    height: 720,
    syncScrolling: "single",
    path: "/static/lib/editormd/editor/lib/",

    // 设置主体颜色
    //theme : "dark",
    //previewTheme : "dark",
    //editorTheme : "pastel-on-dark",

    //codeFold : true,
    //syncScrolling : false,
    saveHTMLToTextarea : true,    // 保存 HTML 到 Textarea

    htmlDecode : "style,script,iframe|on*",            // 开启 HTML 标签解析，为了安全性，默认不开启

    emoji : true,   // 启用emoji表情
    taskList : true,    // 启用tasklist
    tocm : true,         // Using [TOCM]
    tex : true,                   // 开启科学公式TeX语言支持，默认关闭
    flowChart : true,             // 开启流程图支持，默认关闭
    sequenceDiagram : true,       // 开启时序/序列图支持，默认关闭,

    imageUpload: true, //开启图片上传
    imageFormats: ["jpg", "jpeg", "gif", "png", "bmp"], //支持上传的图片格式
    //imageUploadURL: "{% url 'api-upload-url' %}" //处理图片上传的后端URL地址#}
    // 图片上传后可以在onload里做进一步处理
});

$(function (){
    $("textarea").attr('placeholder','博客内容');
});