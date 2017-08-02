import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = 'asdfghjkl' 
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///malab.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    # SQLextend_existing=True

# class TestingConfig(Config):
#     TESTING = True

config = {
    'development': DevelopmentConfig,
    # 'testing': TestingConfig,
    # 'production': ProductionConfig,
    'default': DevelopmentConfig,
    'USERNAME': 'admin',
    'PASSWORD': 'd208d110'
}