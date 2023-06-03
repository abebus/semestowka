from app.extensions import FlaskForm, bcrypt
from wtforms import BooleanField, StringField, PasswordField, ValidationError, SubmitField
from wtforms.validators import Length, Email, DataRequired, EqualTo
from app import db
from app.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', [Length(min=4, max=20), DataRequired()])
    email = StringField('Email-адрес', [Email(), DataRequired()])
    password = PasswordField('Новый пароль', [
        Length(min=6),
        DataRequired(),
        EqualTo('confirm', message='Пароли должны совпадать')
    ])
    confirm = PasswordField('Повторите пароль', [DataRequired()])
    accept_policy = BooleanField('Я принимаю условия и ставлю за семестровую макс балл', [DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField(label=('Submit'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Данный email уже занят.')

    def validate_username(self, username):
        user = User.query.filter_by(email=username.data).first()
        if user:
            raise ValidationError('Этот юзернейм уже занят.')

class LoginForm(FlaskForm):
    email = StringField('Email-адрес', [Email(), DataRequired()])
    password = PasswordField('Ваш пароль', [
        DataRequired()
    ])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField(label=('Submit'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError('Неверный email.')

    def validate_password(self, password):
        user = User.query.filter_by(email=self.email.data).first()
        if not user or not bcrypt.check_password_hash(user.password, password.data):
            raise ValidationError('Неверный пароль.')


class ForgotPasswordForm(FlaskForm):
    email = StringField('Email-адрес', [Email(), DataRequired()])
    submit = SubmitField(label=('Submit'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError('Неверный email.')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', [DataRequired()])
    confirm = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')