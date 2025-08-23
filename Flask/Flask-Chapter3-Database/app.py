from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from sqlalchemy import text

app = Flask(__name__)

# MySQL 配置 - 检查这些值是否正确
HOSTNAME = "127.0.0.1"  # 或者尝试 "localhost"
PORT = 3306
USERNAME = "root"
PASSWORD = "linzhong123"  # 替换为实际密码
DATABASE = "learn"  # 先用默认的 test 数据库

# 重要：确保连接字符串格式正确
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 打印连接字符串以调试
print("数据库连接字符串:", app.config['SQLALCHEMY_DATABASE_URI'])

db = SQLAlchemy(app)

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

# user1 = User(username='张三', password='111111')
# sql: insert user(username,password) values('张三',111111');

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return 'Hello World!'

# @app.route('/test-db')
# def test_db():
#     if test_connection():
#         return '数据库连接成功！'
#     else:
#         return '数据库连接失败！'

if __name__ == '__main__':
    print("正在测试数据库连接...")
    # test_connection()
    app.run(debug=True)