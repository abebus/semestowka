if __name__ == '__main__':
    import app
    import ssl

    socketio = app.socketio

    cert_path = 'cert.pem'
    key_path = 'key.pem'

    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain(cert_path, key_path)

    db = app.db
    app_ = app.create_app()

    with app_.app_context():
        db.create_all()

    # app_.run(debug=True, ssl_context=context)
    socketio.run(app_, debug=True, ssl_context=context, allow_unsafe_werkzeug=True)
