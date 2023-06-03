from flask_mail import Message
from config import Config
import jwt
from app.extensions import mail
from time import time
from app.models import User
from flask import render_template


def get_reset_token(email, expires=500):
    return jwt.encode({'reset_password': email, 'exp': time() + expires}, key=Config.SECRET_KEY, algorithm='HS256')


def send_reset_email(user, token):
    msg = Message()
    msg.subject = "Flask App Password Reset"
    msg.sender = Config.MAIL_USERNAME
    msg.recipients = [user.email]
    msg.html = render_template('mails/reset_email.jinja2',
                               user=user,
                               token=token)
    mail.send(msg)


def verify_reset_token(token):
    try:
        data = jwt.decode(token, key=Config.SECRET_KEY, algorithms=['HS256'])
        print(data)
    except Exception as e:
        print(e)
        return
    return User.query.filter_by(email=data['reset_password']).first()
