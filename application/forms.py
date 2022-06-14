from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

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