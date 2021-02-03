from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir,'.env'))
#configurations for Flask application on development environment only
class Config(object):
    SECRET_KEY = environ.get('SECRET_KEY')
    SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
    FLASK_ENV = 'development'
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'


    # Database configurations
    SQLALCHEMY_DATABASE_URI = environ.get('TENNIS_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
