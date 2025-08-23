# exts.py:这个文件存在的意义就是为了解决循环引用的问题

# flask-sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import redis

db = SQLAlchemy()
mail = Mail()

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True
)

# 如果需要密码认证，可以添加：
# redis_client = redis.Redis(
#     host='localhost',
#     port=6379,
#     password='your_redis_password',
#     db=0,
#     decode_responses=True
# )