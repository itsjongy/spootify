from datetime import datetime, timedelta
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import UserMixin
from .db import db, environment, SCHEMA

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(30), nullable=False, unique=True)
    profile_picture = db.Column(db.String(255))
    status = db.Column(db.String(255))
    status_expiry = db.Column(db.DateTime())
    biography = db.Column(db.String(255))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def set_password(self, password):
        self.password = generate_password_hash(password).decode('utf-8')

    def set_profile_picture(self, filename):
        self.profile_picture = filename

    def set_status(self, status, duration):
        if not status or not isinstance(status, str):
            raise ValueError('Status must be a non-empty string.')
        if duration not in ['1h', '12h', '1d', 'never']:
            raise ValueError('Invalid duration.')
        self.status = status
        if duration == 'never':
            self.status_expiry = None
        else:
            self.status_expiry = datetime.utcnow() + timedelta(hours=int(duration[:-1]))

    def set_biography(self, biography):
        if biography and not isinstance(biography, str):
            raise ValueError('Biography must be a string.')
        self.biography = biography

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    def get_id(self):
        return str(self.id)

def load_user(user_id):
    from . import login_manager
    return User.query.get(int(user_id))
