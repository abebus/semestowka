from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_socketio import SocketIO
from flask_restful import Resource, Api
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_admin import Admin

db = SQLAlchemy()
bcrypt = Bcrypt()
session = Session()
api = Api()
csrf = CSRFProtect()
socketio = SocketIO()
mail = Mail()
admin = Admin(name='Semestrowka', template_mode='bootstrap4')
