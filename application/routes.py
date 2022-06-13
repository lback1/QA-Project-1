from application import app, db
from application.models import Player, PlayerForm, Voter, VoterForm
from flask import render_template, redirect, url_for, request

@app.route('/')
def home():
    return render_template('home.html')