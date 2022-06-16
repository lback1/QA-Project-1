from email import message
from application import app, db
from flask import render_template, redirect, url_for, request
from application.forms import PlayersForm, VotersForm
from application.models import Players, Voters

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/add_players', methods=['GET', 'POST'])
def add_players():
    form = PlayersForm()
    if form.validate_on_submit():
        new_players = Players(players_name=form.players_name.data, position=form.position.data, shirt_number=form.shirt_number.data)
        db.session.add(new_players)
        db.session.commit()
        return render_template('index.html', message="Player Added!")
    else:
        return render_template('add_players.html', form=form)

@app.route('/players_list')
def players_list():
    all_players = Players.query.all()
    return render_template('players_list.html', all_players=all_players)

@app.route('/update_players/<int:id>', methods = ['GET','POST'])
def update_players(id):
    all_players = Players.query.all()
    return render_template('update_players.html', all_players=all_players)

@app.route('/update_one_player/<players_name>', methods = ['GET', 'POST'])
def update_player(player_name):
    form = PlayersForm()
    update_one_player = Players.query.filter_by(player_name=player_name).first()
    if request.method == 'POST':
        if update_one_player:
            update_one_player.player_name = form.player_name.data
            db.session.commit()
            return redirect(url_for('update', message = "Player updated"))
    else:
        return render_template('update_one_player.html', update_one_player=update_one_player, form=form)


@app.route('/delete_players/<int:id>', methods=['GET', 'POST'])
def delete_players(id):
    players = Players.query.filter_by(id=id).first()
    if players:
        db.session.delete(players)
        db.session.commit()
        return redirect(url_for('players_list'))
    else:
        return render_template('players_list.html', id=id)


@app.route('/add_voters', methods=['GET', 'POST'])
def add_voters():
    form = VotersForm()
    if form.validate_on_submit():
        new_voters = Voters(voters_name=form.voters_name.data, reason=form.reason.data, players_id=form.players_id.data)
        db.session.add(new_voters)
        db.session.commit()
        return render_template('index.html', message="Voter Added!")
    else:
        return render_template('add_voters.html', form=form)

@app.route('/voters_list')
def voters_list():
    all_voters = Voters.query.all()
    return render_template('voters_list.html', all_voters=all_voters)

@app.route('/update_voters/<int:id>', methods = ['GET','POST'])
def update_voters(id):
    all_voters = Voters.query.all()
    form = VotersForm()
    if request.method == 'POST':
        update_voters = Voters.query.filter_by(id=id).first()
        if update_voters:
            update_voters.voters_name = request.form['voters_name']
            update_voters.reason = request.form['reason']
            update_voters.players_id = request.form['players_id']
            db.session.commit()
            return render_template('voters_list.html', all_voters=all_voters)
        return f"voter with id = {id} does not exist"
    else:
        return render_template('update_voters.html', form=form, id=id)
    

@app.route('/delete_voters/<int:id>', methods=['GET', 'POST'])
def delete_voters(id):
    voters = Voters.query.filter_by(id=id).first()
    if voters:
        db.session.delete(voters)
        db.session.commit()
        return redirect(url_for('voters_list'))
    else:
        return render_template('voters_list.html', id=id)