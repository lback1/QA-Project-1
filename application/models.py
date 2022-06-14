from application import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(40), nullable=False)
    position = db.Column(db.String(40))
    shirt_number = db.Column(db.Integer)
    voters = db.relationship('Voter', backref='player')

class Voter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    voter_name = db.Column(db.String(40), nullable=False)
    reason = db.Column(db.String(80))
    player_id = db.Column(db.Integer, db.ForiegnKey('player.id'))