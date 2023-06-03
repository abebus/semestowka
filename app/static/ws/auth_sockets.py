from flask import session

def auth_sockets(socketio):
    @socketio.on('connect')
    def connect():
        print('ws connected')


    @socketio.on('disconnect')
    def disconnect():
        if not session.get('remember_me'):
            print('clearing session via ws') # do not work
            session.clear()
            session['authorized'] = False
