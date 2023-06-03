from flask import render_template, redirect, url_for, session
from app.routes.profile import bp
from app.models import User

@bp.route('/')
def index():
    user = User.query.filter_by(id=session.get('user_id')).first()
    return render_template('profile/index.jinja2', user=user)
