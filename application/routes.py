from application import app, db
from application.models import PlayerOfTheSeason, PlayersForm, TeamOfTheSeason, TeamsForm, ManagerOfTheSeason, ManagersForm
from flask import redirect, render_template, request, url_for

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/add_player', methods=['GET', 'POST'])
def add_player():
    form = PlayersForm()
    if form.validate_on_submit():
        new_player = PlayerOfTheSeason(player_name=form.player_name.data, shirt_number=form.shirt_number.data, position=form.position.data)
    db.session.add(new_player)
    db.session.commit()

@app.route('/add_team', methods=['GET', 'POST'])
def add_team():
    form = TeamsForm()
    if form.validate_on_submit():
        new_team = TeamOfTheSeason(team_name=form.team_name.data, country=form.country.data, league=form.league.data)
    db.session.add(new_team)
    db.session.commit()

@app.route('/add_manager', methods=['GET', 'POST'])
def add_manager():
    form = ManagersForm()
    if form.validate_on_submit():
        new_manager = ManagerOfTheSeason(manager_name=form.manager_name.data)
    db.session.add(new_manager)
    db.session.commit()
