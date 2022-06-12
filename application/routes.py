from application import app, db
from application.models import PlayerOfTheSeason, TeamOfTheSeason, ManagerOfTheSeason

@app.route('/')
def home():
    return 