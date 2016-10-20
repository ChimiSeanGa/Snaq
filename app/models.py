from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String, nullable=False, primary_key=True)
    name = db.Column(db.String, nullable=False)
    profile_url = db.Column(db.String, nullable=False)
    access_token = db.Column(db.String, nullable=False)
