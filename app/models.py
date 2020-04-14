from app import db
from datetime import datetime

class User(db.Model):
    id = db. Column (db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    useremail = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    events = db.relationship('Event', backref='host', lazy='dynamic')
    
    def __repr__(self):
        return '<User {}>'.format(self.username)

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