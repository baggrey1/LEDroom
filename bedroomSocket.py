from flask import Flask
from flask.ext.socketio import SocketIO, emit
from LEDroom import setColor

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('connect')
def slider_connect():
    emit('my response', {'data': 'Connected!'})
    print('Client connected')

@socketio.on('json')
def set_colors(colors):
	red = int(colors[0]['intensity'])
	green = int(colors[1]['intensity'])
	blue = int(colors[2]['intensity'])
	setColor(red, green, blue)
	storedColor = colors
	with open('last_color.txt', 'w') as outfile:
		json.dump(storedColor, outfile)

@socketio.on('disconnect')
def slider_disconnect():
    print('Client disconnected')

if __name__ == "__main__":
	socketio.run(app, host='0.0.0.0')
