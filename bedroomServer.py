from flask import Flask, request
from flask.ext.socketio import SocketIO
from LEDroom import boringOn, allOff, setColor, fadeOn
import json

app = Flask(__name__)
socketio = SocketIO(app)

options = {
	'command=on':['Lights on!', boringOn],
	'command=off':['Lights out!', allOff]
}

@app.route('/state/')
def state():
	# This route accepts a string as a GET param and turns lights on/off
	command = request.query_string
	input_list = options.get(command)
	functionToCall = input_list[1]
	functionToCall()
	print(storedColor)

	return input_list[0], 200

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
	storedColor = {
		'red':red,
		'green':green,
		'blue': blue
	}
	with open('last_color.txt', 'w') as outfile:
		json.dump(storedColor, outfile)

@socketio.on('disconnect')
def slider_disconnect():
    print('Client disconnected')

if __name__ == "__main__":
	socketio.run(app, host='0.0.0.0')
