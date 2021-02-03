import unittest
from tennis_score_app import app, db
from test_base_app import BaseTestCaseForTennisScoreApp
from tennis_score_app.models.models import Player, MatchWon

class TestPlayer(BaseTestCaseForTennisScoreApp):
    def test_name(self):
        philip = Player(name='Philip',match_wins=2,match_losses=1,set_wins=9)
        self.assertEqual(philip.name,'Philip')

    def test_wrong_name(self):
        john = Player(name='John',match_wins=2,match_losses=1,set_wins=9)
        self.assertNotEqual(john,'Philip')

    def test_player_in_db(self):
        john = Player(name='John Doe',match_wins=3,match_losses=4,set_wins=8)
        db.session.add(john)
        self.assertIn(john, db.session)

    def test_lookup(self):
        jane = Player(name='Jane Doe', match_wins=4, match_losses=5, set_wins=8)
        db.session.add(jane)
        db.session.commit()
        players = Player.query.all()
        self.assertIn(jane,players)

    def test_total_matches(self):
        phil = Player(name="Phil", match_wins=2, match_losses=2, set_wins=10)
        self.assertEqual(Player.get_total_matches(phil.match_wins,phil.match_losses),4)

    def test_match_wins(self):
        player1 = Player(name="Player1", match_wins=2, match_losses=2, set_wins=10)
        self.assertEqual(player1.match_wins,2)

    def test_match_losses(self):
        player2 = Player(name="Player2", match_wins = 3, match_losses = 4, set_wins=19)
        self.assertEqual(player2.match_losses, 4)

    def test_set_wins(self):
        person = Player(name="Person", match_wins = 3, match_losses = 4, set_wins=20)
        self.assertEqual(person.set_wins, 20)

    #tests player winning 3 tennis matches
    def test_player_match_relationship(self):
        person1 = Player(name="Person1", match_wins = 2, match_losses = 1, set_wins=12)
        match_five_sets = MatchWon(player_won=person1.name,number_of_sets=5,tiebreak_points=5,tennis_player=person1)
        match_three_sets = MatchWon(player_won=person1.name,number_of_sets=3,tiebreak_points=7,tennis_player=person1)
        match_with_10pt_tiebreak = MatchWon(player_won=person1.name,number_of_sets=5,tiebreak_points=10,tennis_player=person1)
        person1.matches_won.append(match_five_sets)
        person1.matches_won.append(match_three_sets)
        person1.matches_won.append(match_with_10pt_tiebreak)
        db.session.add(person1)
        db.session.add(match_five_sets)
        db.session.add(match_three_sets)
        db.session.add(match_with_10pt_tiebreak)
        db.session.commit()
        #player won 3 matches
        self.assertEqual(person1.matches_won.count(),3)

    def test_empty_player_match_relationship(self):
        person = Player(name="Person", match_wins = 4, match_losses = 2, set_wins=12)
        db.session.add(person)
        db.session.commit()
        self.assertEqual(person.matches_won.count(),0)



if __name__ == '__main__':
    unittest.main()
