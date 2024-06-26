from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/chat')
def chat_template():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    print("Mensagem recebida com sucesso")
    socketio.emit('message', message)

if __name__ == "__main__":
    socketio.run(app, debug=True)