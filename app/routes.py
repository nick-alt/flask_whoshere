from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm, RegistrationForm, AttendForm, MessageForm, EventForm, EditEventForm, DeleteEventForm
from flask_login import current_user, login_user, logout_user
from app.models import User, Event, Attendee, Message
from flask_login import login_required
from operator import itemgetter, attrgetter, methodcaller
from app import db



@app.route ('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    #if current_user.is_authenticated:
     #   return redirect(url_for('index'))
    form= LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('invalid username or password')
            return redirect (url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('user', username=current_user.username))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET','POST'])
def register():
   # if current_user.is_authenticated:
    #    return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user= User(username=form.username.data, useremail=form.useremail.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/user/<username>', methods=['GET', 'POST'])
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    form = EventForm()
    
    events = Event.query.filter_by(host=user).order_by(Event.eventdate).all()

    if form.validate_on_submit():
        event = Event(eventname = form.eventname.data, eventdate = form.eventdate.data, host = current_user )
        db.session.add(event)
        db.session.commit()
        flash('You created a new event!')
        return redirect(url_for('user', username=current_user.username))


    return render_template('user.html', form=form, events=events)

@app.route('/attend', methods=['GET', 'POST'])
def attend():
    form = AttendForm()
    if form.validate_on_submit():
        attendee = Attendee(attendeename=form.attendeename.data, attenndeeemail=form.attendeeemail.data)
        db.session.add(attendee)
        db.session.commit()
        flash('you are added to the attendance list!')
    return render_template('attend.html', title= "I'm here", form=form)

@app.route('/message', methods=['GET', 'POST'])
def message():
    form = MessageForm()
    if form.validate_on_submit():
        message = Message(messagesubject=form.messagesubject.data, messagebody=form.messagebody.data)
        db.session.add(message)
        db.session.commit()
        flash('your message was send to the host')
        return redirect (url_for('message'))
    return render_template('message.html', title= 'message', form=form)

@app.route('/event/<event_id>', methods=['GET', 'POST'])
@login_required

def event(event_id):
    event = Event.query.filter_by(id=event_id).first_or_404()
    form = EditEventForm()
    
    if form.validate_on_submit():
        event.eventname = form.eventname.data
        event.eventdate = form.eventdate.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('user', username=current_user.username))
    elif request.method == 'GET':
        form.eventname.data = event.eventname
        form.eventdate.data = event.eventdate
    return render_template('event.html', title='Edit Event',form=form, event=event)

@app.route('/deleteevent/<event_id>', methods=['GET', 'POST'])
@login_required

def deleteevent(event_id):
    event = Event.query.filter_by(id=event_id).first_or_404()
    form = DeleteEventForm()

    if form.validate_on_submit():
        db.session.delete(event)
        db.session.commit()
        flash('you deleted the event')
        return redirect(url_for('user', username=current_user.username))
    return render_template('deleteevent.html', title='Edit Event',form=form, event=event)
