from app.models import User as User_model
from app.extensions import Resource


class User(Resource, User_model):
    def get(self, **kwargs):
        return User_model.query.filter_by(kwargs).all()
