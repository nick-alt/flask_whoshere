from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user
from app.models import User
from flask_login import login_required
from app import db


@app.route ('/')
@app.route('/index')
@login_required
def index():
    events = [
        {
            'event_name' : 'Watte-Party',
            'body': '50 Attendees'
        },
        {
            'event_name' : 'Triaden',
            'body': '37 Attendees'

        }

    ]
    return render_template('index.html', title='Homy', events=events)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form= LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('invalid username or password')
            return redirect (url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user= User(username=form.username.data, email=form.useremail.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    events=[
        {'host': user, 'eventname': 'Testevent1'},
        {'host': user, 'eventname': 'Testevent1'}
     ]
     return render_template('user.html', user=user, events=events)