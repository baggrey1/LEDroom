from flask import Flask, request
from flask.ext.socketio import SocketIO
from LEDroom import boringOn, allOff, setColor

app = Flask(__name__)
socketio = SocketIO(app)

# define globals
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

	return input_list[0], 200

@socketio.on('connect')
def slider_connect():
    emit('my response', {'data': 'Connected!'})
    print('Client connected')

@socketio.on('json')
def set_colors(colors):
	red = colors[0].get(intensity)
	green = colors[1].get(intensity)
	blue = colors[2].get(intensity)
	setColor(red,green,blue)
	print('changed red value: '+str(red))

@socketio.on('disconnect')
def slider_disconnect():
    print('Client disconnected')

if __name__ == "__main__":
	socketio.run(app, host='0.0.0.0')
