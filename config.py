import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.urandom(32) #os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"
    SERVER_NAME = '127.0.0.1:11111'
    CLIENT_ID = '62345cebb3972c13a312'
    CLIENT_SECRET = '123e4e3a2d5337e4e18e57e1ec79d52fd675e1ab'
    SOCIAL_AUTH_REDIRECT_IS_HTTPS = True

    # Установите параметр SESSION_COOKIE_SECURE в True, чтобы куки сессии передавались только через HTTPS
    SESSION_COOKIE_SECURE = True

    # Установите параметр SESSION_COOKIE_HTTPONLY в True, чтобы куки были недоступны для JavaScript
    SESSION_COOKIE_HTTPONLY = True

    # Установите время жизни сессии, например, на 1 час
    PERMANENT_SESSION_LIFETIME = 3600

    # Установите параметр SESSION_COOKIE_SAMESITE в 'Lax' или 'Strict'
    SESSION_COOKIE_SAMESITE = 'Lax'

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'abebus.semestowka@gmail.com'
    MAIL_PASSWORD = 'zbltzagpmrnahogw'

    GOOGLE_CLIENT_ID = '835113143349-8ie4ec1vvbfojpua673vehba7g5d12i6.apps.googleusercontent.com'
    GOOGLE_CLIENT_SECRET = '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'