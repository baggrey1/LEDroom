from flask import Flask, request, jsonify
from flask.ext.cors import CORS
from LEDroom import boringOn, setColor, fade
import json

options = {
	'command=on':['Lights on!', 'on'],
	'command=off':['Lights out!', 'off']
}

def state():
	print 'running debug script'
	# This route accepts a string as a GET param and turns lights on/off
	command = 'command=off'
	input_list = options.get(command)
	# Read previous command from text file
	with open('last_command.txt') as infile:    
		last_command = infile.read().strip('0')
		print last_command

	with open('last_color.txt') as infile:
		storedColor = json.load(infile)

	if command != last_command:
		print 'command != last_command'		
		stateToSend = input_list[1]
		fade(stateToSend)

	# Store command in text file
	with open('last_command.txt','w') as outfile:
		outfile.write("0{0}".format(command))

state()
