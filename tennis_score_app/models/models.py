#declaration of tennis player model
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from tennis_score_app import db
"""
There are two tables in this database:
Player and Match.
These two tables have a relationship:
More specifically: a one-to-many relationship
These two tables have this relationship because one player can win
many matches. This relationship establishes a record of a player that wins many matches.
"""

class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column('player_id',db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    #number of match wins
    match_wins = db.Column(db.Integer)
    #number of match losses
    match_losses = db.Column(db.Integer)
    #total number of sets player won
    set_wins = db.Column(db.Integer)
    matches_won = db.relationship('MatchWon', back_populates='player', lazy='dynamic')

    def __init__(self,name, match_wins, match_losses, set_wins):
        self.name = name
        self.match_wins = match_wins
        self.match_losses = match_losses
        self.set_wins = set_wins

    @staticmethod
    def get_total_matches(match_wins,match_losses):
        return match_wins + match_losses

    def __repr__(self):
        return '<Name: {}>'.format(self.name)


class MatchWon(db.Model):
    __tablename__ = 'match_won'
    match_id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    #total max number of sets in tennis match.
    number_of_sets = db.Column(db.Integer)
    player_won = db.Column(db.String(90),nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('players.player_id'))
    tiebreak_points = db.Column(db.Integer)#tiebreak number to break the tie
    player = db.relationship('Player')

    def __init__(self, player_won, number_of_sets,tiebreak_points,tennis_player):
        self.player_won = player_won
        self.number_of_sets = number_of_sets
        self.tiebreak_points = tiebreak_points
        self.tennis_player = tennis_player

    def __repr__(self):
        return '<Win:{0}><Max Sets:{1}><Tiebreak Points:{2}>'.format(self.player_won,self.number_of_sets,self.tiebreak_points)
