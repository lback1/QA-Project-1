from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class PlayerOfTheSeason(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(40), nullable=False)
    team_id = db.Column('TeamOfTheSeason_id', db.Integer, db.ForiegnKey('TeamOfTheSeason_id'))
    manager_id = db.Column('ManagerOfTheSeason_id', db.Interger, db.ForiegnKey('ManagerOfTheSeason_id'))
    shirt_number = db.Column(db.Interger)
    position = db.Column(db.String(40))
    manageroftheseason = db.relationship('Manager', backref='playerbr')
    teamoftheseason = db.relationship('Team', backref='playererbr')

class TeamOfTheSeason(db.Model):
    id = db.Column(db.Interger, primary_key=True)
    team_name = db.Column(db.String(40), nullable=False)
    country = db.Column(db.String(40))
    league = db.Column(db.String(40))
    trophies_won = db.Column(db.Interger)
    manager_id = db.Column('ManagerOfTheSeason_id', db.Interger, db.ForiegnKey('ManagerOfTheSeason_id'))
    manageroftheseason = db.relationship('Manager', backref='teambr')

class ManagerOfTheSeason(db.Model):
    id = db.Column(db.Interger, primary_key=True)
    manager_name = db.Column(db.String(40), nullable=False)
    team_id = db.Column('TeamOfTheSeason_id', db.Integer, db.ForiegnKey('TeamOfTheSeason_id'))
    teamoftheseason = db.relationship('Team', backref='managerbr')

class PlayersForm(FlaskForm):
    player_name = StringField('Enter the player name', validators=[DataRequired()])
    team_id = IntegerField('Team information')
    manager_id = IntegerField('Manager information')
    shirt_number = IntegerField('Enter the shirt number')
    position = StringField('Enter the position')
    submit = SubmitField('Add')

class TeamsForm(FlaskForm):
    team_name = StringField('Enter the team name', validators=[DataRequired()])
    country = StringField('Enter the country')
    league = StringField('Enter the league')
    trophies_won = IntegerField('Enter the number of trophies won')
    manager_id = IntegerField('Manager information')
    submit = SubmitField('Add')

class ManagersForm(FlaskForm):
    manager_name = StringField('Enter the manager name', validators=[DataRequired()])
    team_id = IntegerField('Team information')
    submit = SubmitField('Add')

