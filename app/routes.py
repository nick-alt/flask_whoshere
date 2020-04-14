from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route ('/')
@app.route('/index')
def index():
    user = {'username': 'Alaida'}
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
    return render_template('index.html', title='Homy', user=user, events=events)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form= LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}' .format(form.username.data, form.remember_me.data))
        return redirect (url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
