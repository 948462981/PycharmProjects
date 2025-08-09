from flask import Flask, render_template, request

# web应用程序
app = Flask(__name__)


# 访问到127.0.0.1:5000
# @app.route('/')
# def index():
#     return "hello world"
#
# @app.route('/hello')
# def hello():
#     return "hello world hello world hello world"

# 引入模板 -> html
# @app.route('/')
# def index():
#     return render_template("hello.html") # 自动的找templates文件夹里的hello.html文件

# # 把一个变量传送到页面
# @app.route('/')
# def index():
#     n = "Not Hello World"
#     list = ["1", "2", "3",  "4", "5"]
#     return render_template("hello.html", new=n, list=list) # 自动的找templates文件夹里的hello.html文件


# 通过一个案例来学习如何从页面接收数据
# 登录验证
@app.route('/')
def index():
    return render_template("login.html")
@app.route('/login', methods=["POST"])
def login():
    # 接收到用户名和密码
    username = request.form.get("username")
    password = request.form.get("pwd")
    if username == "xxx" and password == "123456":
        return "登录成功"
    else:
        return render_template("login.html", msg="用户名或密码错误")


if __name__ == '__main__':
    app.run(debug=True)