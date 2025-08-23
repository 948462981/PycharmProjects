from flask_sqlalchemy import SQLAlchemy

SECRET_KEY = "dsmnfdsmwemkrdsmvkllcfdjkhgk"

# 数据库的配置信息
HOSTNAME = "127.0.0.1"  # 或者尝试 "localhost"
PORT = 3306
USERNAME = "root"
PASSWORD = "linzhong123"  # 替换为实际密码
DATABASE = "OA_learn"

DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

# 重要：确保连接字符串格式正确
# app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# 邮箱配置
MAIL_SERVER = "smtp.googlemail.com"
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = "948462981qq@gmail.com"
MAIL_PASSWORD = "wyxfugcbhwxwndsb"
MAIL_DEFAULT_SENDER = "948462981qq@gmail.com"
# wyxf ugcb hwxw ndsb

