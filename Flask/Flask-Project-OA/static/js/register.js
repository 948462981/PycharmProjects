function bindEmailCaptchaClick(){
    $("#send-captcha").click(function (event){
        // $this 代表的是当前按钮的jquery对象
        var $this = $(this)
        // 阻止默认的事件
        event.preventDefault();

        var email = $("input[name='email']").val();
        // 显示用户输入的邮箱 - 您要求的功能
        // alert('用户输入的邮箱: ' + email);

        $.ajax({
            // http://127.0.0.1:500
            // /auth/captcha/email?email=xx@qq.com
            url: "/auth/captcha/email?email="+email,
            method: "GET",
            success: function (result){
                var code = result['code'];
                if (code == 200){
                    var countdown = 5;
                    $this.off("click");
                    var timer = setInterval(function (){
                        $this.text(countdown);
                        countdown -= 1;
                        // 倒计时结束的时候执行
                        if (countdown <= 0){
                            // 清掉计算器
                            clearInterval(timer);
                            // 将按钮的文字重新修改回来
                            $this.text("获取验证码");
                            // 重新绑定点击事件
                            bindEmailCaptchaClick();
                        }
                    }, 1000);
                    // alert("邮箱验证码发送成功")
                }else {
                    alert(result['message']);
                }
            },
            fail: function (error){
                console.log(error);
            }
        });
    });
}


// 整个网页都加载完毕再执行
$(function (){
    bindEmailCaptchaClick();
});