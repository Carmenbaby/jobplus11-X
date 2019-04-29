from flask_wtf import FlaskForm
from wtforms.validators import Length, Email, EqualTo, Required
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, IntegerField, TextAreaField, SelectField


class RegisterForm(FlaskForm):
    name = StringField('???', validators=[Required(), Length(3, 24)])
    email = StringField('??', validators=[Required(), Email()])
    password = PasswordField('??', validators=[Required(), Length(6, 24)])
    repeat_password = PasswordField('????', validators=[Required(), EqualTo('password')])
    submit = SubmitField('??')

    def validate_username(self, field):
        if User.query.filter_by(name=field.data).first():
            raise ValidationError('??????')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('??????')

    def create_user(self):
        user = User(name=self.name.data,
                    email=self.email.data,
                    password=self.password.data)
        db.session.add(user)
        db.session.commit()
        return user