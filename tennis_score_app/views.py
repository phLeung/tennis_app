from flask import Flask,render_template, request
from flask import redirect, url_for
from tennis_score_app import app, db
from models.models import Player
from models.models import MatchWon
point_winner_list = []
server_list = []


#decorator for home route
@app.route("/")
def home():
    return render_template("submit_match_form.html")

@app.route("/score_pt", methods=['POST'])
def score_tennis_match():
    player1_name = request.form['player1_name']
    player2_name = request.form['player2_name']
    number_of_sets = request.values['sets']
    tiebreaker_points = request.values['tiebreaker']
    return render_template("score_tracker.html", player1_name = player1_name, player2_name = player2_name,
      number_of_sets=number_of_sets, tiebreaker_points=tiebreaker_points)

@app.route("/receiveinfo", methods=['POST'])
def receive_info():
    global point_winner_list
    global server_list
    point_winner_list.append(request.form['point_winner'])
    server_list.append(request.form['player_serve'])
    return "OK"
