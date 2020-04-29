from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User, Attendee
from wtforms.fields.html5 import DateField

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    useremail = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class AttendForm(FlaskForm):
    attendeename = StringField('Name', validators=[DataRequired()])
    attendeeemail = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Attend')

class MessageForm(FlaskForm):
    messagebody = TextAreaField('Your message', validators=[DataRequired(), Length(min=1, max=200)])
    submit = SubmitField('Send Message')

class EventForm(FlaskForm):
    eventname = StringField('Event Name', validators=[DataRequired()])
    eventdate = DateField('Event Date', format='%Y-%m-%d')
    submit = SubmitField('Create Event')

class EditEventForm(FlaskForm):
    eventname = StringField('Event Name', validators=[DataRequired()])
    eventdate = DateField('Event Date', format='%Y-%m-%d')
    submit = SubmitField('Edit Event')

class DeleteEventForm(FlaskForm):
    confirm = BooleanField('Are You Sure?', validators=[DataRequired()])
    submit = SubmitField ('Delete Event')

class EditMessageForm(FlaskForm):
    messagebody = TextAreaField('Edit message', validators=[DataRequired(), Length(min=1, max=200)])
    submit = SubmitField('Edit Message')

class HostMessage(FlaskForm):
    messagebody = TextAreaField('Your message', validators=[DataRequired(), Length(min=1, max=200)])
    submit = SubmitField('Send Message')

class ForwardMessage(FlaskForm):
    submit =SubmitField('Forward Message')
    
