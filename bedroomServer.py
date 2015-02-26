from flask import Flask
from ouimeaux.environment import Environment
from ouimeaux.signals import statechange, receiver
from LEDroom import boringOn, allOff

app = Flask(__name__)

env = Environment()

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
	env.start()
	env.discover(5)
	switch = env.get_switch('bedroomSwitch')

	@receiver(statechange, sender=switch)
	def switch_toggle(device, **kwargs):
		print device, kwargs['state']
		if kwargs['state'] == 1:
			boringOn()

		else:
			allOff()

	env.wait()