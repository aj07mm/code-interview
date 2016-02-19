#The origin (0,0) can be considered to be the SOUTH WEST most corner

def robot(commands):
	table = get_clear_table()
	table_bound_x = table_bound_y = 4 # -1 considering 0 as first index
	current_pos_x = current_pos_y = current_pos_f = None

	#check if there is commands
	if(len(commands)>0):
		if('PLACE' not in commands[0]):
			commands = slice_PLACE_as_first_command(commands)
		for command in commands:
			command = parse_command(command)
			table = get_clear_table()
			if(command['PLACE']):
				if(check_bound(command['PLACE']['place_y'], table_bound_y, 0) and check_bound(command['PLACE']['place_x'], table_bound_x, 0)):
					current_pos_x = command['PLACE']['place_x']
					current_pos_y = command['PLACE']['place_y']
					current_pos_f = command['PLACE']['place_f']
					table[current_pos_x][current_pos_y] = current_pos_f
				continue
			if(command['MOVE']):
				if(current_pos_f == 'NORTH'):
					if(check_bound(current_pos_y, table_bound_y, 1)):
						current_pos_x = current_pos_x
						current_pos_y = current_pos_y + 1
				if(current_pos_f == 'SOUTH'):
					if(check_bound(current_pos_y, table_bound_y, -1)):
						current_pos_x = current_pos_x
						current_pos_y = current_pos_y - 1
				if(current_pos_f == 'EAST'):
					if(check_bound(current_pos_x, table_bound_x, 1)):
						current_pos_x = current_pos_x + 1
						current_pos_y = current_pos_y
				if(current_pos_f == 'WEST'):
					if(check_bound(current_pos_x, table_bound_x, -1)):
						current_pos_x = current_pos_x - 1
						current_pos_y = current_pos_y
				table[current_pos_x][current_pos_y] = current_pos_f
				continue
			if(command['LEFT']): #rotate
				if(current_pos_f == 'NORTH'):
					current_pos_f = 'WEST'
				elif(current_pos_f == 'WEST'):
					current_pos_f = 'SOUTH'
				elif(current_pos_f == 'SOUTH'):
					current_pos_f = 'EAST'
				elif(current_pos_f == 'EAST'):
					current_pos_f = 'NORTH'
				table[current_pos_x][current_pos_y] = current_pos_f
				continue
			if(command['RIGHT']): #rotate
				if(current_pos_f == 'NORTH'):
					current_pos_f = 'EAST'
				elif(current_pos_f == 'EAST'):
					current_pos_f = 'SOUTH'
				elif(current_pos_f == 'SOUTH'):
					current_pos_f = 'WEST'
				elif(current_pos_f == 'WEST'):
					current_pos_f = 'NORTH'
				table[current_pos_x][current_pos_y] = current_pos_f
				continue
			if(command['REPORT']): #rotate
				if(current_pos_x != None and current_pos_y != None and current_pos_f != None):
					print current_pos_x, current_pos_y, current_pos_f
	return table

def slice_PLACE_as_first_command(commands):
	PLACE_index = False
	for command in commands:
		if 'PLACE' in command:
			PLACE_index = commands.index(command)

	if(PLACE_index):
		return commands[PLACE_index:]

	return []

def check_bound(current_pos_axis, axis_bound, increment):
	if(current_pos_axis + increment > axis_bound):
		return False
	if(current_pos_axis + increment < 0):
		return False
	return True

def check_command(command):
	parsed_object = parse_command(command)
	return not all(val==False for val in parsed_object.values()) 

def get_clear_table():
	table = [
		['','','','',''],
		['','','','',''],
		['','','','',''],
		['','','','',''],
		['','','','',''],
	]
	return table

def parse_command(command):
	#possible_commands
	output_command = {
		'PLACE': False,
		'MOVE': False,
		'LEFT': False,
		'RIGHT': False,
		'REPORT': False
	}
	possible_facing = [
		'NORTH',
		'SOUTH',
		'EAST',
		'WEST'
	]
	if('PLACE' in command):
		place_command = command.split(' ')
		if(len(place_command) > 1):
			place_command_part1 = place_command[0]
			place_command_part2 = place_command[1].split(',')
			if(place_command_part1 == 'PLACE' and len(place_command_part2) == 3):
				place_x = place_command_part2[0]
				place_y = place_command_part2[1]
				place_f = place_command_part2[2]
				if(place_f in possible_facing):
					output_command['PLACE'] = {}
					output_command['PLACE']['place_x'] = int(place_x)
					output_command['PLACE']['place_y'] = int(place_y)
					output_command['PLACE']['place_f'] = place_f

	if('MOVE' == command):
		output_command['MOVE'] = True
	#rotate
	if('LEFT' == command):
		output_command['LEFT'] = True
	if('RIGHT' == command):
		output_command['RIGHT'] = True
	if('REPORT' == command):
		output_command['REPORT'] = True

	return output_command