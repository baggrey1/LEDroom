# this server sends and receives all signals from wemo switches.
# It makes RESTful calls to other services in the apartment based on the switch states
# Date: 3/23/2015
# Author: Brian Aggrey

import requests
from ouimeaux.environment import Environment
from ouimeaux.signals import statechange, receiver

# define globals
bedroomURL = 'http://192.168.1.2:5000'

if __name__ == "__main__":
	env.start()
	env.discover(5)
	switch = env.get_switch('bedroomSwitch')

	@receiver(statechange, sender=switch)
	def switch_toggle(sender, **kwargs):
		print sender.name, kwargs['state']
		if kwargs.get('state'):
			# If switch turns on, send GET request to bedroomServer with "on" param
			requests.get(bedroomURL + '/state/', params = {
				'command': 'on'
				})

		else:
			# If switch turns on, send GET request to bedroomServer with "off" param
			requests.get(bedroomURL + '/state/', params = {
				'command': 'off'
				})			

	env.wait()