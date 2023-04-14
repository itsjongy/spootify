from app.models import db, User

def seed_users():
    # create 5 users
    users = [
        User(username="demo", email="demo@gmail.com", password="demo"),
        User(username="jongy", email="jongy@gmail.com", password="jongy"),
        User(username="phamgoesham", email="phamgoesham@gmail.com", password="password"),
        User(username="jxde", email="jaden@gmail.com", password="password"),
        User(username="johnnybutt", email="johnnybutt@gmail.com", password="password")
    ]

    # add the users to the session and commit
    for user in users:
        existing_user = User.query.filter_by(email=user.email).first()
        if existing_user is None:
            db.session.add(user)

    db.session.commit()

def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
