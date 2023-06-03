from dataclasses import dataclass
from app.extensions import db
from enum import IntEnum


@dataclass
class User(db.Model):
    __tablename__ = 'user'
    id: int
    login: str
    email: str
    password: str
    role: str
    has_token: bool
    has_additional_info: bool
    additional_info: dict

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.Text, unique=True)
    email = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)
    role = db.Column(db.Text, nullable=False, default='user')
    has_token = db.Column(db.Boolean, default=False)
    has_additional_info = db.Column(db.Boolean, default=False)
    additional_info = db.Column(db.JSON, default='')


@dataclass
class Diary(db.Model):
    __tablename__ = 'diary'
    id: int
    user_id: int
    school_id: int
    content_json: dict

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    school_id = db.Column(db.Integer)
    content_json = db.Column(db.JSON)

@dataclass
class Subject(db.Model):
    id: int
    name: str

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


Weekdays = IntEnum('Weekdays', 'sun mon tue wed thu fri sat', start=0)


@dataclass
class Day(db.Model):
    id: int
    diary_id: int
    week_day: Weekdays
    subjects: dict

    id = db.Column(db.Integer, primary_key=True)
    diary_id = db.Column(db.Integer)
    week_day = db.Column(db.Integer)
    subjects = db.Column(db.JSON)

