from flask_wtf import FlaskForm
from wtforms.validators import Length, Email, EqualTo, Required
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, IntegerField, TextAreaField, SelectField
from jobplus.models import db,User

class RegisterForm(FlaskForm):
    name = StringField('用户名', validators=[Required(), Length(3, 24)])
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码', validators=[Required(), Length(6, 24)])
    repeat_password = PasswordField('重复密码', validators=[Required(), EqualTo('password')])
    submit = SubmitField('提交')

    def validate_username(self, field):
        if User.query.filter_by(name=field.data).first():
            raise ValidationError('用户名已存在')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已存在')

    def create_user(self):
        user = User(name=self.name.data,
                    email=self.email.data,
                    password=self.password.data)
        db.session.add(user)
        db.session.commit()
        return user


class LoginForm(FlaskForm):
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码', validators=[Required(), Length(6, 24)])
    remember_me = BooleanField('重复')
    submit = SubmitField('提交')

    def validate_email(self, field):
        if field.data and not User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱不存在或未注册')

    def validate_password(self, field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('密码错误')
