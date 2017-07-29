import os

# DATABASE = os.path.join(os.path.curdir, 'malab.db'),


class Config(object):
    DEBUG = False
    TESTING = False
    # DATABASE_URI = 'sqlite://:memory:'

class Admin(Config):
    ADMIN = 'malabadmin'
    PASSWORD = 'd208d110'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
