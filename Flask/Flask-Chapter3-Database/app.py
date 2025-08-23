from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from sqlalchemy import text
from flask_migrate import Migrate

app = Flask(__name__)

# MySQL 配置 - 检查这些值是否正确
HOSTNAME = "127.0.0.1"  # 或者尝试 "localhost"
PORT = 3306
USERNAME = "root"
PASSWORD = ""  # 替换为实际密码
DATABASE = "learn"  # 先用默认的 test 数据库

# 重要：确保连接字符串格式正确
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 打印连接字符串以调试
print("数据库连接字符串:", app.config['SQLALCHEMY_DATABASE_URI'])

db = SQLAlchemy(app)

migrate = Migrate(app, db)
# ORM模型映射成表的三步
# 1.flask db init:这步只需要执行一次, python -m flask db upgrade
# 2.flask db migrate:识别ORM模型的改变，生成迁移脚本
# 3.flask db upgrade:将迁移脚本应用到数据库中


# def test_connection():
#     try:
#         with app.app_context():
#             result = db.session.execute(text('SELECT 1 as test'))
#             row = result.fetchone()
#             print("数据库连接成功:", row)
#             return True
#     except Exception as e:
#         print("数据库连接失败:", str(e))
#         return False

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False) # varchar(), NOT NULL
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100))
    signature = db.Column(db.String(200))

# user1 = User(username='张三', password='111111')
# sql: insert user(username,password) values('张三',111111');

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False) # varchar(), NOT NULL
    content = db.Column(db.Text, nullable=False)

    # 添加作者的外键
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    # backref 会自动给User添加一个属性articles，用来获取文章列表
    author = db.relationship('User', backref='articles')


# article.author_id = user.id
# user = User.query.get(article.author_id)
# print(article.author)


# with app.app_context():
#     db.drop_all()
#     db.create_all()


@app.route('/')
def index():
    return 'Hello World!'

# @app.route('/test-db')
# def test_db():
#     if test_connection():
#         return '数据库连接成功！'
#     else:
#         return '数据库连接失败！'

@app.route('/user/add')
def add_user():
    # 1. 创建对象
    user1 = User(username='张三', password='111111')
    # 2. 将ORM对象添加到db.session中
    db.session.add(user1)
    # 3. 将db.session中的改变同步到数据库中
    db.session.commit()
    return '用户添加成功！'

@app.route('/user/query')
def query_user():
    # 1. get查找：根据主键
    # user = User.query.get(1)
    # print(f"{user.id}: {user.username} - {user.password}")
    # 2. filter_by查找
    # Query: 类数组
    users = User.query.filter_by(username='张三')
    for user in users:
        print(user.username)
    return "数据查找成功"

@app.route('/user/update')
def update_user():
    user = User.query.filter_by(username='张三').first()
    user.password = "222222"
    db.session.commit()
    return "数据修改成功"

@app.route('/user/delete')
def delete_user():
    user = User.query.get(1)
    db.session.delete(user)
    db.session.commit()
    return "数据删除成功"

@app.route('/article/add')
def add_article():
    article1 = Article(title='测试文章', content='这是测试文章的内容')
    article1.author = User.query.get(2)
    article2 = Article(title='Flask', content='Flask内容')
    article2.author = User.query.get(2)
    # 添加到session中
    db.session.add_all([article1, article2])
    db.session.commit()
    return "文章添加成功"

@app.route('/article/query')
def query_article():
    user = User.query.get(2)
    for article in user.articles:
        print(article.title)
    return "文章查询成功"


if __name__ == '__main__':
    print("正在测试数据库连接...")
    # test_connection()
    app.run(debug=True)