from dotenv import load_dotenv
load_dotenv()


import os

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY') 
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_KEY') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.sendgrid.net'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'apikey'
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = 'whoshere.berlin@gmail.com'
