from application import app, db
from application.models import Player, PlayerForm, Voter, VoterForm
from flask import render_template, redirect, url_for, request

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/add_player', methods=['GET', 'POST'])
def add_player():
    form = PlayerForm()
    if form.validate_on_submit():
        new_player = Player(player_name=form.player_name.data, position=form.position.data, shirt_number=form.shirt_number.data)
        db.session.add(new_player)
        db.session.commit()
        return redirect(url_for('add_player'))
    else:
        return render_template('add_player.html', form=form)

@app.route('/view_player')
def view_player():
    all_players = Player.query.all()
    return render_template('player_list.html', all_players=all_players)

@app.route('/update_player/<int:id>', methods = ['GET','PUT'])
def update_player(id):
    all_players = Player.query.all()
    form = PlayerForm()
    if request.method == 'POST':
        update_player = Player.query.filter_by(id=id).first()
        if update_player:
            update_player.player_name = request.form['player_name']
            update_player.position = request.form['position']
            update_player.shirt_number = request.form['shirt_number']
            db.session.commit()
            return render_template('player_list.html', all_players=all_players)
        return f"player with id = {id} does not exist"
    else:
        return render_template('update_player.html', form=form, id=id)


@app.route('/delete_player/<int:id>', methods=['GET', 'DELETE'])
def delete_player(id):
    player = Player.query.filter_by(id=id).first()
    if player:
        db.session.delete(player)
        db.session.commit()
        return redirect(url_for('player_list'))
    else:
        return render_template('player_list.html', id=id)


@app.route('/add_voter', methods=['GET', 'POST'])
def add_voter():
    form = VoterForm()
    if form.validate_on_submit():
        new_voter = Voter(voter_name=form.voter_name.data, reason=form.reason.data, player_id=form.player_id.data)
        db.session.add(new_voter)
        db.session.commit()
        return redirect(url_for('add_voter'))
    else:
        return render_template('add_voter.html', form=form)

@app.route('/view_voter')
def read():
    all_voters = Voter.query.all()
    return render_template('voter_list.html', all_voters=all_voters)

@app.route('/update_voter/<int:id>', methods = ['GET','PUT'])
def update_voter(id):
    all_voters = Voter.query.all()
    form = VoterForm()
    if request.method == 'POST':
        update_voter = Voter.query.filter_by(id=id).first()
        if update_voter:
            update_voter.voter_name = request.form['voter_name']
            update_voter.reason = request.form['reason']
            update_voter.player_id = request.form['player_id']
            db.session.commit()
            return render_template('voter_list.html', all_voters=all_voters)
        return f"voter with id = {id} does not exist"
    else:
        return render_template('update_voter.html', form=form, id=id)
    

@app.route('/delete_voter/<int:id>', methods=['GET', 'DELETE'])
def delete_voter(id):
    voter = Voter.query.filter_by(id=id).first()
    if voter:
        db.session.delete(voter)
        db.session.commit()
        return redirect(url_for('voter_list'))
    else:
        return render_template('voter_list.html', id=id)