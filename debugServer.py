options = {
	'command=on':['Lights on!', fadeOn],
	'command=off':['Lights out!', allOff]
}

def state():
	# This route accepts a string as a GET param and turns lights on/off
	command = 'command=on'
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