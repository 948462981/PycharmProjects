from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/profile')
def profile():
    return 'It is your profile page.'

@app.route('/blog/list')
def blog_list():
    return 'It is your blog list page.'

@app.route('/blog/<int:blog_id>')
def blog_detail(blog_id):
    return f"您的访问博客是：{blog_id}"

#查询字符串的方式传参
#/book/list:会给我返回第一页的数据
# #/book/list?page=2:获取第二页的数据
@app.route('/book/list')
def book_list():
    # request.args 类字典
    page = request.args.get('page', default=1, type=int)
    return f"您获取的是第{page}页的图书列表"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)