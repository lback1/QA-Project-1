from application import db
from application.models import Player, Voter

db.drop_all()
db.create_all()

player1 = Player(player_name="Declan Rice", position="CDM", shirt_number="41")

db.session.add(player1)
db.session.commit()

voter1 = Voter(voter_name="Luke", reason="best player", player_id=player1.id)

db.session.add(voter1)
db.session.commit()