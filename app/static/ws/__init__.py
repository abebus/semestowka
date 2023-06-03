from app.static.ws import auth_sockets, profile_sockets

def register_socket_handlers(socketio):
    auth_sockets.auth_sockets(socketio)
    # profile_sockets.profile_sockets(socketio)