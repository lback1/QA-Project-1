from application import db

class PlayerOfTheSeason(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    playerName = db.Column(db.String(30))
    teamName = db.Column(db.String(30), foriegn_key=True)
    

