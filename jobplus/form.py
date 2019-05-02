from flask_wtf import FlaskForm
from wtforms.validators import Length, Email, EqualTo, Required
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, IntegerField, TextAreaField, SelectField
from flask_wtf.file import FileField, FileRequired, FileAllowed
import os
from jobplus.models import db,User,CompanyDetail

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
    remember_me = BooleanField('记住')
    submit = SubmitField('提交')

    def validate_email(self, field):
        if field.data and not User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱不存在或未注册')

    def validate_password(self, field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('密码错误')

class UserProfileForm(FlaskForm):
    real_name = StringField('姓名',validators=[Required(), Length(6,24)])
    email = StringField('邮箱',validators=[Required(), Email()])
    password = PasswordField('密码（不修改无需填写）')
    phone = StringField('手机号码')
    work_years = IntegerField('工作年限')
    resume = StringField('简历地址')
    submit = SubmitField('提交')

    def validate_phone(self, field):
        phone = field.data
        if len(phone) != 11:
            raise ValidationError('请输入正确的手机号码')

    def upload_resume(self):
        f = self.resume.data
        filename = self.real_name.data + '.pdf'
        #save:将文件保存到服务器。
        f.save(os.path.join(
            os.getcwd(),
            'static',
            'resumes',
            filename
        ))
        
        return filename

    def update_profile(self, user):
        user.real_name = self.real_name.data
        user.email = self.email.data
        if self.password.data:
            user.password = self.password.data
        user.phone = self.phone.data
        user.work_years = self.work_years.data
        #filename = self.upload_resume()
        user.resume_url = self.resume.data#url_for('static', filename=os.path.join('resumes', filename))
        db.session.add(user)
        db.session.commit()

class CompanyProfileForm(FlaskForm):
    name = StringField('企业名称')
    email = StringField('邮箱', validators=[Required(), Email()])
    phone = StringField('手机号')
    password = PasswordField('密码(不填写保持不变)')

    location = StringField('地址', validators=[Required(),Length(0, 64)])
    logo = StringField('Logo',validators=[Required()])
    site = StringField('公司网站', validators=[Required(),Length(0, 64)])

    description = StringField('一句话描述', validators=[Length(0, 100)])
    about = TextAreaField('公司详情', validators=[Length(0, 1024)])
    submit = SubmitField('提交')

    def validate_phone(self, field):
        phone = field.data
        if len(phone) != 11:
            raise ValidationError('请输入正确的手机号码')

    def updated_profile(self, user):
        user.name = self.name.data
        user.email = self.email.data
        user.phone = self.phone.data
        if self.password.data:
            user.password = self.password.data
        if user.detail:
            detail = user.detail
        else:
            detail = CompanyDetail()
            detail.user_id = user.id
        self.populate_obj(detail)
        db.session.add(user)
        db.session.add(detail)
        db.session.commit()