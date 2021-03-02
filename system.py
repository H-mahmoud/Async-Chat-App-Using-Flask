from flask import session
from application.app import create_app
from flask_socketio import SocketIO, send, join_room
from datetime import datetime

app = create_app()
socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.on('connected', namespace="/chat_room")
def check_connection(msg):
    room = session['ip']
    join_room(room)
    print('Message: ' + msg)


@socketio.on('message', namespace="/chat_room")
def check_connection(msg):
    now = datetime.now()
    time = now.strftime("%H:%M")
    
    room = session["ip"]
    msg = {"name": session["name"], "msg": msg, "time": time}
    send(msg, room=room)
    

if __name__ == '__main__':
	socketio.run(app)