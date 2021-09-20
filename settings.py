"""Application Configuration"""
import os

class Config(object):
    SECRET_KEY = "uhsgfjnfioyvhiudenfvfwsiuttuydhg"
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    CORS_ORIGIN_WHITELIST = [
        'http://0.0.0.0:4100',
        'http://0.0.0.0:3000',
        'http://localhost:4100',
        'http://localhost:3000',
        'http://0.0.0.0:8000',
        'http://localhost:8000',
        'http://0.0.0.0:4200',
        'http://localhost:4200',
        'http://0.0.0.0:4000',
        'http://localhost:4000',
    ]


class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'
    # DEBUG = False
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',
    #                                          'postgresql://localhost/example')
    DB_NAME = 'dev.db'
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)
