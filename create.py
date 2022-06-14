from application import db
from application.models import Players, Voters

db.drop_all()
db.create_all()