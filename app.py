from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = '!secret'

socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/phone')
def phone():
    return render_template('phone.html')

@app.route('/tablet')
def tablet():
    return render_template('tablet.html')

@socketio.on('button_click')
def handle_button_click(data):
    emit('update_phone', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)