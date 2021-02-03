import unittest
from tennis_score_app import app, db
from test_base_app import BaseTestCaseForTennisScoreApp
from tennis_score_app.models.models import MatchWon
from tennis_score_app.models.models import Player

class TestMatchWon(BaseTestCaseForTennisScoreApp):

    def test_player_won(self):
        player2 = Player(name="Player2", match_wins = 3, match_losses = 4, set_wins=19)
        match1 = MatchWon(player_won=player2.name, number_of_sets=5, tiebreak_points=7,tennis_player=player2)
        self.assertEqual(match1.player_won,"Player2")

    def test_number_of_sets(self):
        player1 = Player(name="Player1", match_wins = 4, match_losses = 1, set_wins=9)
        french_match = MatchWon(player_won=player1.name, number_of_sets = 5, tiebreak_points=5,tennis_player=player1)
        self.assertEqual(french_match.number_of_sets,5)

    def test_tiebreak_points(self):
        person1 = Player(name="Person1", match_wins = 5, match_losses = 2, set_wins=5)
        tennis_match = MatchWon(player_won=person1.name, number_of_sets=3, tiebreak_points=5,tennis_player=person1)
        self.assertEqual(tennis_match.tiebreak_points,5)

    def test_lookup(self):
        john = Player(name="John Doe", match_wins = 5, match_losses = 1, set_wins=20)
        australian_match = MatchWon(player_won=john.name, number_of_sets = 5, tiebreak_points=10,tennis_player=john)
        db.session.add(australian_match)
        db.session.commit()
        matches = MatchWon.query.all()
        self.assertIn(australian_match, matches)

    def test_match_in_db(self):
        nigel = Player(name="Nigel", match_wins = 19, match_losses = 11, set_wins=25)
        british_match = MatchWon(player_won=nigel.name, number_of_sets = 3, tiebreak_points=5,tennis_player=nigel)
        db.session.add(british_match)
        self.assertIn(british_match,db.session)

if __name__ == '__main__':
    unittest.main()
