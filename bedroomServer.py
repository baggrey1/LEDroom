from flask import Flask, request
from flask.ext.socketio import SocketIO
from LEDroom import boringOn, allOff, setColor, fadeOn

app = Flask(__name__)
socketio = SocketIO(app)

# define globals
storedColor = {
	'red': 255,
	'green': 255,
	'blue':255
}

options = {
	'command=on':['Lights on!', fadeOn(storedColor)],
	'command=off':['Lights out!', allOff]
}

@app.route('/state/')
def state(storedColor):
	# This route accepts a string as a GET param and turns lights on/off
	command = request.query_string
	input_list = options.get(command)
	functionToCall = input_list[1]
	functionToCall()
	print(storedColor)

	return input_list[0], 200, storedColor

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

@socketio.on('disconnect')
def slider_disconnect():
    print('Client disconnected')

if __name__ == "__main__":
	socketio.run(app, host='0.0.0.0', debug=true)
