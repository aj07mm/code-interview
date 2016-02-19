import csv, sys
from robot import robot, check_command

print '#########################'
print '## Toy Robot Simulator ##'
print '######### IMPORT ########'
print '#########################'
print ''
print ''

filename = sys.argv[1]
commands = []

with open(filename) as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print row['command']
		if(check_command(row['command'])):
			commands.append(row['command'])
		else:
			print 'Wrong command, try again'

print 'Output:'
robot(commands)