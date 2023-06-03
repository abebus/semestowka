import app
from app import socketio

app = socketio(app.create_app())
