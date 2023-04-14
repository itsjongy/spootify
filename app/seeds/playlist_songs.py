from app.models import db, Playlist, Song, PlaylistSong

def seed_playlist_songs():
    # get the demo playlist
    demo_playlist1 = Playlist.query.filter_by(title="beep boops").first()
    demo_playlist2 = Playlist.query.filter_by(title="head bobbers").first()

    # get some songs
    song1 = Song.query.filter_by(title="Blinding Lights").first()
    song2 = Song.query.filter_by(title="Crawl Outta Love").first()
    song3 = Song.query.filter_by(title="Emotion Sickness").first()
    song4 = Song.query.filter_by(title="Shape Of You").first()
    song5 = Song.query.filter_by(title="Uptown Funk").first()

    # create playlist songs
    playlist_song1 = PlaylistSong(playlist=demo_playlist1, song=song2)
    playlist_song2 = PlaylistSong(playlist=demo_playlist1, song=song3)
    playlist_song3 = PlaylistSong(playlist=demo_playlist2, song=song1)
    playlist_song4 = PlaylistSong(playlist=demo_playlist2, song=song4)
    playlist_song5 = PlaylistSong(playlist=demo_playlist2, song=song5)

    # add the playlist songs to the session and commit
    db.session.add_all([playlist_song1, playlist_song2, playlist_song3, playlist_song4, playlist_song5])
    db.session.commit()

def undo_playlist_songs():
    db.session.execute('TRUNCATE playlist_songs RESTART IDENTITY CASCADE;')
    db.session.commit()
