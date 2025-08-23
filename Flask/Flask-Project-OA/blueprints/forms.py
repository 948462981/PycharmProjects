import wtforms
from wtforms.validators import Email, Length, EqualTo, input_required, InputRequired
from models import UserModel
from exts import redis_client

# Forms： 验证前端提交的数据是否符合要求
class RegisterForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误")])
    captcha = wtforms.StringField(validators=[Length(min=4, max=4, message="验证码长度错误")])
    username = wtforms.StringField(validators=[Length(min=3, max=20, message="用户名长度错误")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="密码长度错误")])
    password_confirm = wtforms.StringField(validators=[EqualTo("password", message="密码不一致")])

    # 自定义验证：
    # 1. 邮箱是否已被注册
    # 2. 验证码是否正确
    def validate_email(self, field):
        email = field.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="邮箱已被注册")

    def validate_captcha(self, field):
        captcha = field.data  # 用户输入的验证码
        email = self.email.data  # 获取邮箱字段的值

        # 构造 Redis 键名（与 auth.py 中保持一致）
        redis_key = f"email_captcha:{email}"

        # 从 Redis 中获取存储的验证码
        stored_captcha = redis_client.get(redis_key)

        # 检查验证码是否存在（可能已过期）
        if not stored_captcha:
            raise wtforms.ValidationError(message="验证码已过期或不存在")

        # 检查验证码是否匹配（不区分大小写）
        if captcha.lower() != stored_captcha.lower():
            raise wtforms.ValidationError(message="验证码错误")

        # 验证通过后，可以选择删除验证码（防止重复使用）
        redis_client.delete(redis_key)


class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="密码长度错误")])


class QuestionForm(wtforms.Form):
    title = wtforms.StringField(validators=[Length(min=3, max=100, message="标题长度错误")])
    content = wtforms.StringField(validators=[Length(min=3, message="内容长度太短")])

class AnswerForm(wtforms.Form):
    content = wtforms.StringField(validators=[Length(min=3, message="内容长度太短")])
    question_id = wtforms.IntegerField(validators=[InputRequired(message="必须要传入问题id")])
