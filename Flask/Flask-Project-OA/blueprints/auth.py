# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Blueprint, render_template, jsonify, redirect, url_for, session
from flask_mail import Message
from exts import mail, db, redis_client
from flask import request
import string
import random
# from models import EmailCaptchaModel
from .forms import RegisterForm, LoginForm
from models import UserModel
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                print("邮箱在数据库中不存在")
                return redirect(url_for("auth.login"))
            if check_password_hash(user.password, password):
                print("密码正确")
                # cookie:
                # cookie中不适合存储太多数据，只适合存储少量数据
                # cookie 一般用来存储用户名，用户ID，用户权限等信息。
                # flask中的session，是经过加密后存储在cookie中的
                session["user_id"] = user.id
                return redirect("/")
            else:
                print("密码错误")
                return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.login"))


# GET: 从服务器上获取数据。
# Post：向服务器提交数据。
@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        # 验证用户提交的邮箱和验证码是否对应且正确
        # 表单验证: flask-wtf: wtforms
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            username = form.username.data
            user = UserModel(email=email, password=generate_password_hash(password), username=username)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.register"))


@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("qa.index"))

@bp.route("/captcha/email")
def get_email_captcha():
    # /captcha/email/<email>
    # /captcha/email?email=xxx@gmail.com
    email = request.args.get("email")
    if not email:
        return jsonify({"code": 400, "message": "邮箱地址不能为空", "data": None})

    # 4/6: 随机数字，字母，数字和字母的组合
    source = string.digits * 4
    captcha = random.sample(source, 4)
    captcha = "".join(captcha)
    # I/O: Input/Output
    message = Message(
        subject="注册验证码",
        recipients=[email],
        body=f"验证码是:{captcha}"
    )
    mail.send(message)

    # memcached/redis
    # 用数据库存储
    # email_captcha = EmailCaptchaModel(email=email, captcha=captcha)
    # db.session.add(email_captcha)
    # db.session.commit

    # 使用 Redis 存储验证码，设置5分钟过期时间
    redis_key = f"email_captcha:{email}"
    redis_client.setex(redis_key, 300, captcha)  # 300秒 = 5分钟

    return jsonify({"code": 200, "message": "验证码发送成功", "data": None})

# @bp.route("/mail/test")
# def mail_test():
#     message = Message(
#         subject="948462981qq@gmail.com",
#         recipients=["yufenglin2002@gmail.com"],
#         body="This is a test email."
#     )
#     mail.send(message)
#     return "Email sent!"