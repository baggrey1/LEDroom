from flask import Flask, request, jsonify
from flask.ext.cors import CORS
from LEDroom import boringOn, allOff, setColor, fadeOn
import json


app = Flask(__name__)
CORS(app)

options = {
	'command=on':['Lights on!', fadeOn],
	'command=off':['Lights out!', allOff]
}

@app.route('/state/')
def state():
	# This route accepts a string as a GET param and turns lights on/off
	command = request.query_string
	input_list = options.get(command)
	# Read previous command from text file
	with open('last_command.txt') as infile:    
		last_command = infile.read().strip('0')

	with open('last_color.txt') as infile:
		storedColor = json.load(infile)

	if command != last_command:		
		functionToCall = input_list[1]
		functionToCall()

	# Store command in text file
	with open('last_command.txt','w') as outfile:
		outfile.write("0{0}".format(command))

	return input_list[0], 200

@app.route('/last-state/')
def last_state():
	# This route returns the most recent state and color upon GET
	with open('last_command.txt') as command_file:
		last_command = command_file.read().strip('0')

	with open('last_color.txt') as color_file:
		last_color = json.load(color_file)

	last_state_obj = {
		'lastCommand': last_command,
		'lastColor': last_color
	}

	return jsonify(last_state_obj), 200

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5555, debug=True)