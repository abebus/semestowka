from flask import Flask

from config import Config
from app.extensions import db, api, csrf, session, bcrypt, socketio, mail, admin


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    session.init_app(app)
    api.init_app(app)
    csrf.init_app(app)
    bcrypt.init_app(app)
    socketio.init_app(app)
    mail.init_app(app)
    admin.init_app(app)

    from app.static.ws import register_socket_handlers
    register_socket_handlers(socketio)

    # Register blueprints here
    from app.routes.admin import register_admin_views
    register_admin_views()

    from app.routes.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.routes.auth import bp as login_bp
    app.register_blueprint(login_bp, url_prefix='/auth')

    from app.routes.diary import bp as diary_bp
    app.register_blueprint(diary_bp, url_prefix='/school-diary')

    from app.routes.profile import bp as profile_bp
    app.register_blueprint(profile_bp, url_prefix='/profile')

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app
