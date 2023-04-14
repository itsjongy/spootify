from app.models import db, Playlist, User

def seed_playlists():
    # get the demo user
    demo_user = User.query.filter_by(username="demo_user").first()

    # create some playlists
    playlist1 = Playlist(title="beep boops", user=demo_user, image_url="https://online.berklee.edu/takenote/wp-content/uploads/2018/09/aditya-chinchure-494048-unsplash-1024x768.jpg")
    playlist2 = Playlist(title="head bobbers", user=demo_user, image_url="https://i1.sndcdn.com/artworks-000248384985-fqivuk-t500x500.jpg")

    # add the playlists to the session and commit
    db.session.add_all([playlist1, playlist2])
    db.session.commit()

def undo_playlists():
    db.session.execute('TRUNCATE playlists RESTART IDENTITY CASCADE;')
    db.session.commit()
