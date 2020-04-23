from app import app, db
from app.models import User, Event, Attendee, Message

if __name__ == '__main__':
    app.run(host="0.0.0.0")
    
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User':User, 'Event':Event, 'Attendee':Attendee, 'Message':Message}
