from flask import Blueprint

bp = Blueprint('school-diary', __name__)

from app.routes.diary import routes
