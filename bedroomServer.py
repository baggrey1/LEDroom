from flask import Flask, request
from flask.ext.socketio import SocketIO
from LEDroom import boringOn, allOff, setColor
from flask.ext.cors import CORS

app = Flask(__name__)
socketio = SocketIO(app)
cors = CORS(app)

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

@socketio.on('connect', namespace='/slider')
def slider_connect():
    emit('my response', {'data': 'Connected!'})

@socketio.on('json', namespace='/slider')
def set_colors(colors):
	setColor(colors[0][intensity],colors[1][intensity],colors[2][intensity])	

@socketio.on('disconnect', namespace='/slider')
def slider_disconnect():
    print('Client disconnected')

if __name__ == "__main__":
	socketio.run(app,debug=True, host='0.0.0.0')
