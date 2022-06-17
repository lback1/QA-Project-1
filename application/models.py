from application import db

class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    players_name = db.Column(db.String(40), nullable=False)
    position = db.Column(db.String(40))
    shirt_number = db.Column(db.Integer)
    voters = db.relationship('Voters', backref='players')

class Voters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    voters_name = db.Column(db.String(40), nullable=False)
    reason = db.Column(db.String(80))
    players_id = db.Column(db.Integer, db.ForeignKey('players.id'))
