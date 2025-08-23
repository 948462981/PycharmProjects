from flask import Flask, session, g
import config
from exts import db, mail
from models import UserModel
from blueprints.qa import bp as qa_bp
from blueprints.auth import bp as auth_bp
from flask_migrate import Migrate

app = Flask(__name__)
# 绑定配置文件
app.config.from_object(config)

db.init_app(app)
mail.init_app(app)

migrate = Migrate(app, db)
# ORM模型映射成表的三步
# 1.flask db init:这步只需要执行一次, python -m flask --app app.py db init
# 2.flask db migrate:识别ORM模型的改变，生成迁移脚本
# 3.flask db upgrade:将迁移脚本应用到数据库中

app.register_blueprint(qa_bp)
app.register_blueprint(auth_bp)


# blueprint
# 电源，音乐，读书，xxx

# before_request, before_first_request, after_request
# hook
@app.before_request
def my_before_request():
    user_id = session.get('user_id')
    if user_id:
        user = db.session.get(UserModel, user_id)
        setattr(g, 'user', user)
    else:
        setattr(g, 'user', None)


@app.context_processor
def my_context_processor():
    return {'user': g.user}


if __name__ == '__main__':
    app.run(debug=True)
