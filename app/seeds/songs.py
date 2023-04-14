from app.models import db, Song
import base64

def seed_songs():
    # create a list of songs
    songs = [
        {
            "title": "Blinding Lights",
            "artist": "The Weeknd",
            "album": "After Hours",
            "release_date": "2019-11-29",
            "cover_photo": "https://i.scdn.co/image/ab67616d0000b2738863bc11d2aa12b54f5aeb36",
            "audio_file": open('/home/jason/appacademy/spookify-official/app/seeds/songs/Blinding Lights.mp3', 'rb').read()
        },
        {
            "title": "Crawl Outta Love",
            "artist": "Illenium, Annika Wells",
            "album": "Awake",
            "release_date": "2017-09-21",
            "cover_photo": "https://upload.wikimedia.org/wikipedia/en/7/75/Awake_Illenium_album.jpg",
            "audio_file": open('/home/jason/appacademy/spookify-official/app/seeds/songs/Crawl Outta Love.mp3', 'rb').read()
        },
        {
            "title": "Emotion Sickness",
            "artist": "Said The Sky, Parachute, Will Anderson",
            "album": "Sentiment",
            "release_date": "2022-02-18",
            "cover_photo": "https://i1.sndcdn.com/artworks-DefvNAzCrhe35oAM-CKKoSg-t500x500.jpg",
            "audio_file": open('/home/jason/appacademy/spookify-official/app/seeds/songs/Emotion Sickness.mp3', 'rb').read()
        },
        {
            "title": "Shape of You",
            "artist": "Ed Sheeran",
            "album": "÷",
            "release_date": "2017-01-06",
            "cover_photo": "https://upload.wikimedia.org/wikipedia/en/b/b4/Shape_Of_You_%28Official_Single_Cover%29_by_Ed_Sheeran.png",
            "audio_file": open('/home/jason/appacademy/spookify-official/app/seeds/songs/Shape Of You.mp3', 'rb').read()
        },
        {
            "title": "Uptown Funk",
            "artist": "Mark Ronson, Bruno Mars",
            "album": "Uptown Special",
            "release_date": "2014-11-10",
            "cover_photo": "https://cdns-images.dzcdn.net/images/cover/3734366a73152d0367a83a4b09fd163f/500x500.jpg",
            "audio_file": open('/home/jason/appacademy/spookify-official/app/seeds/songs/Uptown Funk.mp3', 'rb').read()
        }
    ]

    # add the songs to the session and commit
    for song in songs:
        existing_song = Song.query.filter_by(title=song['title']).first()
        if existing_song is None:
            with open(f"/home//appacademy/spookify-official/app/seeds/songs/{song['title']}.mp3", 'rb') as f:
                song_data = f.read()
            new_song = Song(title=song['title'], artist=song['artist'], album=song['album'],
                            release_date=song['release_date'], cover_photo=song['cover_photo'], audio_file=song_data)
            db.session.add(new_song)

    db.session.commit()

# define an undo_songs() function to delete all songs from the database
def undo_songs():
    db.session.execute('TRUNCATE songs RESTART IDENTITY CASCADE;')
    db.session.commit()
