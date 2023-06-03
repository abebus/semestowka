from app.extensions import admin, db
from app.models import User, Diary, Subject
from flask_admin.contrib.sqla import ModelView
from flask import redirect, url_for, session

class View(ModelView):
    def is_accessible(self):
        print('admin wanna to enter' ,session.get('uid'))
        if session.get('user_id'):
            user = User.query.filter_by(id=session.get('user_id')).first()
            print(user)
            if user:
                print(user.role == 'site-admin')
                return user.role == 'site-admin'
            return False
        else:
            print('you are not admin')
            return False

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('auth.login'))


def register_admin_views():
    admin.add_view(View(User, db.session, name='User'))
    admin.add_view(View(Diary, db.session, name='Diary'))
    admin.add_view(View(Subject, db.session, name='Subject'))


