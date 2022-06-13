from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(40), nullable=False)
    position = db.Column(db.String(40))
    shirt_number = db.Column(db.Integer)
    voters = db.relationship('Voter', backref='playerbr')

class Voter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    voter_name = db.Column(db.String(40), nullable=False)
    reason = db.Column(db.String(80))
    player_id = db.Column('Player_id', db.Integer, db.ForiegnKey('Player_id'))

class PlayerForm(FlaskForm):
    player_name = StringField('Enter the player name', validators=[DataRequired()])
    position = StringField('Enter the position')
    shirt_number = IntegerField('Enter the shirt number')
    submit = SubmitField('submit')

class VoterForm(FlaskForm):
    voter_name = StringField('Enter your name', validators=[DataRequired()])
    reason = StringField('Enter the reason for your vote')
    player_id = IntegerField('Enter player id')
    submit = SubmitField('submit')