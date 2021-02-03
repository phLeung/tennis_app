from flask import Flask
from flask_testing import TestCase
from tennis_score_app import app, db

#this test case class is to be inherited by other
#test case classes
#this class just creates the app and the database
#for testing purposes
class BaseTestCaseForTennisScoreApp(TestCase):
    def create_app(self):
        app.config.from_object('config.TestingConfig')
        return app
    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
