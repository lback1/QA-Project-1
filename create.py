from application import db
from application.models import Player, PlayerForm, Voter, VoterForm

db.drop_all()
db.create_all()