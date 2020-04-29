from flask_mail import Message
from app import mail, app
from flask import render_template

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)


def send_attend_email(attendee,event):
    send_email('[Whoshere] You signed up',
                sender=app.config['MAIL_DEFAULT_SENDER'],
                recipients=[attendee.attendeeemail],
                text_body=render_template('email/attend_event.txt', attendee=attendee, event=event), 
                html_body=render_template('email/attend_event.html', attendee=attendee, event=event)) 


def send_newmessage_email(user,event,message, recipient):
    send_email('[Whoshere] New Message',
                sender=app.config['MAIL_DEFAULT_SENDER'],
                recipients=[recipient],
                text_body=render_template('email/new_message.txt', user=user, event=event, message=message), 
                html_body=render_template('email/new_message.html', user=user, event=event, message=message)) 

def forward_message(event, message, recipient, user):
    send_email('[Whoshere] New Message',
                sender=app.config['MAIL_DEFAULT_SENDER'],
                recipients=recipient,
                text_body=render_template('email/forward_message.txt', event=event, message=message, recpient=recipient), 
                html_body=render_template('email/forward_message.html', event=event, message=message, recpient=recipient)) 