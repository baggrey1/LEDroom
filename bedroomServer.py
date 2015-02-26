from flask import Flask
app = Flask(__name__)

# define globals
options = {
	'command=on':['lights on!', boringOn()],
	'command=off':['lights off!', allOff()]
}


@app.route('/state/')
def state():
	# This route accepts a string as a GET param and turns lights on/off
	command = request.query_string
	input_list = options.get(command)
	input_list[1]

	return input_list[0], 200

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')