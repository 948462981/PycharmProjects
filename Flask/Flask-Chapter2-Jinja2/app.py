from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# 关键点：函数在这里被直接定义了
def datetime_format(value, format="%Y-%m-%d %H:%M"):
    return value.strftime(format)

# 然后，这个刚刚在上面定义好的函数被注册为过滤器
app.add_template_filter(datetime_format, "dformat")

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

@app.route('/')
def index():
    user1 = User('张三', 18)
    person = {
        "name": "ABC",
        "age": "12"
    }
    return render_template('index.html', user1=user1, person=person)

@app.route('/blog/<blog_id>')
def blog_detail(blog_id):
    return render_template('blog_detail.html', blog_id=blog_id)

@app.route('/filter')
def filter():
    user2 = User('qwertyuiop', 19)
    mytime = datetime.now() # 当地时间
    return render_template('filter.html', user2=user2, mytime=mytime)

@app.route('/control')
def control():
    user3 = User('王五', 14)
    mylist = [1, 2, 3, 4, 5]
    return render_template('control.html', user3=user3, mylist=mylist)

@app.route('/child1')
def child1():
    return render_template('child1.html')

@app.route('/child2')
def child2():
    return render_template('child2.html')

@app.route('/static')
def static_demo():
    return render_template('static.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)