import unittest
import os
from tennis_score_app import app
class TestConfiguration(unittest.TestCase):
    def test_development_config(self):
        app.config.from_object('config.DevelopmentConfig')
        assert app.config['DEBUG']
        assert not app.config['TESTING']
        assert app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get('TENNIS_URI')

    def test_testing_config(self):
        app.config.from_object('config.TestingConfig')
        assert app.config['DEBUG']
        assert app.config['TESTING']
        assert not app.config['PRESERVE_CONTEXT_ON_EXCEPTION']
        assert app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get('TENNIS_URI')

    def test_production_config(self):
        app.config.from_object('config.ProductionConfig')
        assert not app.config['DEBUG']
        assert not app.config['TESTING']
        assert app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get('TENNIS_URI')


if __name__ == '__main__':
    unittest.main()
