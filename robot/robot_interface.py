from robot import robot, check_command

print '#########################'
print '## Toy Robot Simulator ##'
print '####### INTERFACE #######'
print '#########################'
print ''
print ''

print 'Input a sequence of commands by typing each one and pressing enter:'

command = None
commands = []

while(command != ''):
	command = raw_input()
	if(check_command(command)):
		commands.append(command)
	else:
		print 'Wrong command, try again'

print 'Output:'
robot(commands)