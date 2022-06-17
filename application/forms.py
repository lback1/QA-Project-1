from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired
from application.models import Players, Voters

class PlayersForm(FlaskForm):
    players_name = StringField('Enter the player name', validators=[DataRequired()])
    position = StringField('Enter the position')
    shirt_number = IntegerField('Enter the shirt number')
    submit = SubmitField('submit')

class VotersForm(FlaskForm):
    voters_name = StringField('Enter your name', validators=[DataRequired()])
    reason = StringField('Enter the reason for your vote')
    players_id = IntegerField('Enter player id')
    submit = SubmitField('submit')