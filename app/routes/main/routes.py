from flask import render_template, redirect, url_for, session
from app.routes.main import bp
from app.models import User

@bp.route('/')
def index():
    uid = session.get('user_id')
    user = User.query.filter_by(id=uid).first()
    if session.get('authorized') and user:
        match user.role:
            case 'teacher':
                return render_template('', user=user)
            case 'student':
                return render_template('index.jinja2', navlinks=[('school-diary', 'строница дневника')], user=user)
            case 'principal':
                return render_template('index.jinja2', user=user)
            case 'site-admin':
                return render_template('index.jinja2', navlinks=[('admin', 'Admin page'), ('school-diary', 'строница дневника')], user=user)
            case _:
                return render_template('index.jinja2', user=user)
    return redirect(url_for('auth.login'))
