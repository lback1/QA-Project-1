from application import db

class PlayerOfTheSeason(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(40), nullable=False)
    team_id = db.Column('TeamOfTheSeason_id', db.Integer, db.ForiegnKey('TeamOfTheSeason_id'))
    manager_id = db.Column('ManagerOfTheSeason_id', db.Interger, db.ForiegnKey('ManagerOfTheSeason_id'))
    shirt_number = db.Column(db.Interger)
    position = db.Column(db.String(40))

class TeamOfTheSeason(db.Model):
    id = db.Column(db.Interger, primary_key=True)
    team_name = db.Column(db.String(40), nullable=False)
    country = db.Column(db.String(40))
    league = db.Column(db.String(40))
    trophies_won = db.Column(db.Interger)
    manager_id = db.Column('ManagerOfTheSeason_id', db.Interger, db.ForiegnKey('ManagerOfTheSeason_id'))

class ManagerOfTheSeason(db.Model):
    id = db.Column(db.Interger, primary_key=True)
    manager_name = db.Column(db.String(40), nullable=False)
    team_id = db.Column('TeamOfTheSeason_id', db.Integer, db.ForiegnKey('TeamOfTheSeason_id'))


    

