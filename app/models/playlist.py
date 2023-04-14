from .db import db, environment, SCHEMA
from datetime import datetime


class Playlist(db.Model):
    __tablename__ = "playlists"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    image_url = db.Column(db.String(255), nullable=False, default='https://community.spotify.com/t5/image/serverpage/image-id/55829iC2AD64ADB887E2A5/image-size/large?v=v2&px=999')
    created_at = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)

    songs = db.relationship('PlaylistSong', back_populates='playlist', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "user_id": self.user_id,
            "image_url": self.image_url,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        }

    def is_owned_by(self, user):
        return user.id == self.user_id
