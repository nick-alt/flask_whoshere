import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '015777233653'
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.sendgrid.net'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'apikey'
    MAIL_PASSWORD = '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'
    MAIL_DEFAULT_SENDER = 'whoshere.berlin@gmail.com'
