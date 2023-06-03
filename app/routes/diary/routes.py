from flask import render_template, redirect, url_for, session
from app.routes.diary import bp
from app.models import User

@bp.route('/')
def index():
    return render_template('diary/index.jinja2')
