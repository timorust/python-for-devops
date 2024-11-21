from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

votes = {"Option 1": 0, "Option 2": 0, "Option 3": 0}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('vote')
def handle_vote(data):
    option = data['option']
    if option in votes:
        votes[option] += 1
        emit('update', {'votes': votes}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
