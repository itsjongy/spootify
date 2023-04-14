from .db import db, environment, SCHEMA

class PlaylistSong(db.Model):
    __tablename__ = "playlist_songs"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)

    playlist = db.relationship("Playlist", back_populates="playlist_songs")
    song = db.relationship("Song", back_populates="playlist_songs")

    def to_dict(self):
        return {
            "id": self.id,
            "playlist_id": self.playlist_id,
            "song_id": self.song_id,
        }
