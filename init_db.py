from app.models import *

def create_empty_db(app, db):
    with app.app_context():
        db.drop_all()
        db.create_all()


def populate_db(app, db):
    with app_.app_context():
        password = app.bcrypt.generate_password_hash('admin')
        db.session.add(User(login='admin', email='admin@admin.admin', password=password, role='site-admin'))
        db.session.commit()

if __name__ == '__main__':
    import app

    app_ = app.create_app()
    db = app.db

    create_empty_db(app_, db)
    populate_db(app, db)
