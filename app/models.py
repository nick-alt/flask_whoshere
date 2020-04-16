from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


class User(UserMixin, db.Model):
    id = db.Column (db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    useremail = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    event_id = db.Column(db.String(10))
    events = db.relationship('Event', backref='host', lazy='dynamic')
    email = db.Column(db.String(10))
    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eventname = db.Column(db.String(64), index=True, unique=True)
    eventdate = db.Column(db.DateTime, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    eventtimestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    attendees = db.relationship('Attendee', backref='attendee', lazy='dynamic')
    messages = db.relationship('Message', backref='event', lazy='dynamic')
    
    def __repr__(self):
        return '<Event {}>'.format(self.eventname)

class Attendee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    attendeename = db.Column(db.String(64), index=True, unique=True)
    attendeeemail = db.Column(db.String(120), index=True, unique=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    attendeetimestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Attendee {}>'.format(self.attendeename)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    messagesubject = db.Column(db.String(40))
    messagebody = db.Column(db.String(200))
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    messagetimestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
         return '<Message {}>'.format(self.messagesubject)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
    