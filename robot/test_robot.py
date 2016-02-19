# coding: utf-8
import unittest
from robot import robot, get_clear_table, parse_command, check_bound

class TestRobot(unittest.TestCase):
	def test_return_table(self):
		commands = []
		self.assertIsInstance(robot(commands), list)
	def test_initial_command_right(self):
		commands = [
			'PLACE X,Y,F'
		]
		self.assertIsInstance(robot(commands), list)
	def test_initial_command_wrong(self):
		commands = [
			'LEFT'
		]
		self.assertEqual(robot(commands), get_clear_table())
	def test_PLACE_done_wrong(self):
		commands = [
			'PLACE 0,0,WESTSIDE'
		]
		self.assertEqual(robot(commands), get_clear_table())
	def test_PLACE_done_incomplete(self):
		commands = [
			'PLACE 0,0'
		]
		self.assertEqual(robot(commands), get_clear_table())
	def test_PLACE_done_incomplete_2(self):
		commands = [
			'PLACE 0'
		]
		self.assertEqual(robot(commands), get_clear_table())
	def test_PLACE_done_incomplete_3(self):
		commands = [
			'PLACE'
		]
		self.assertEqual(robot(commands), get_clear_table())
	def test_initial_command_wrong_then_PLACE(self):
		commands = [
			'LEFT',
			'PLACE 0,0,NORTH'
		]
		output_table = [
			['NORTH','','','',''],
			['','','','',''],
			['','','','',''],
			['','','','',''],
			['','','','',''],
		]
		self.assertEqual(robot(commands), output_table)
	def test_PLACE_0_0_NORTH(self):
		commands = [
			'PLACE 0,0,NORTH'
		]
		output_table = [
			['NORTH','','','',''],
			['','','','',''],
			['','','','',''],
			['','','','',''],
			['','','','',''],
		]
		self.assertEqual(robot(commands), output_table)
	def test_PLACE_0_0_SOUTH(self):
		commands = [
			'PLACE 0,0,SOUTH'
		]
		output_table = [
			['SOUTH','','','',''],
			['','','','',''],
			['','','','',''],
			['','','','',''],
			['','','','',''],
		]
		self.assertEqual(robot(commands), output_table)
	def test_PLACE_0_0_FOO(self):
		commands = [
			'PLACE 0,0,FOO'
		]
		output_table = [
			['','','','',''],
			['','','','',''],
			['','','','',''],
			['','','','',''],
			['','','','',''],
		]
		self.assertEqual(robot(commands), output_table)
	def test_PLACE_0_0_NABOO(self):
		commands = [
			'PLACE 0,0,NABOO'
		]
		output_table = [
			['','','','',''],
			['','','','',''],
			['','','','',''],
			['','','','',''],
			['','','','',''],
		]
		self.assertEqual(robot(commands), output_table)
	def test_MOVE_NORTH(self):
		commands = [
			'PLACE 0,0,NORTH',
			'MOVE'
		]
		output_table = get_clear_table()
		output_table[0][0] = ''
		output_table[0][1] = 'NORTH'
		self.assertEqual(robot(commands), output_table)
	def test_MOVE_SOUTH(self):
		commands = [
			'PLACE 0,0,SOUTH',
			'MOVE'
		]
		output_table = get_clear_table()
		output_table[0][0] = 'SOUTH'
		#output_table[0][-1] = 'SOUTH' FALL
		self.assertEqual(robot(commands), output_table)
	def test_MOVE_WEST(self):
		commands = [
			'PLACE 0,0,WEST',
			'MOVE'
		]
		output_table = get_clear_table()
		output_table[0][0] = 'WEST'
		#output_table[-1][0] = 'WEST' FALL
		self.assertEqual(robot(commands), output_table)
	def test_MOVE_EAST(self):
		commands = [
			'PLACE 0,0,EAST',
			'MOVE'
		]
		output_table = get_clear_table()
		output_table[0][0] = ''
		output_table[1][0] = 'EAST'
		self.assertEqual(robot(commands), output_table)
	def test_rotate_NORTH_LEFT(self):
		commands = [
			'PLACE 0,0,NORTH',
			'LEFT'
		]
		output_table = get_clear_table()
		output_table[0][0] = 'WEST'
		self.assertEqual(robot(commands), output_table)
	def test_rotate_WEST_LEFT(self):
		commands = [
			'PLACE 0,0,WEST',
			'LEFT'
		]
		output_table = get_clear_table()
		output_table[0][0] = 'SOUTH'
		self.assertEqual(robot(commands), output_table)
	def test_rotate_SOUTH_LEFT(self):
		commands = [
			'PLACE 0,0,SOUTH',
			'LEFT'
		]
		output_table = get_clear_table()
		output_table[0][0] = 'EAST'
		self.assertEqual(robot(commands), output_table)
	def test_rotate_EAST_LEFT(self):
		commands = [
			'PLACE 0,0,EAST',
			'LEFT'
		]
		output_table = get_clear_table()
		output_table[0][0] = 'NORTH'
		self.assertEqual(robot(commands), output_table)
	def test_rotate_NORTH_RIGHT(self):
		commands = [
			'PLACE 0,0,NORTH',
			'RIGHT'
		]
		output_table = get_clear_table()
		output_table[0][0] = 'EAST'
		self.assertEqual(robot(commands), output_table)
	def test_rotate_EAST_RIGHT(self):
		commands = [
			'PLACE 0,0,EAST',
			'RIGHT'
		]
		output_table = get_clear_table()
		output_table[0][0] = 'SOUTH'
		self.assertEqual(robot(commands), output_table)
	def test_rotate_SOUTH_RIGHT(self):
		commands = [
			'PLACE 0,0,SOUTH',
			'RIGHT'
		]
		output_table = get_clear_table()
		output_table[0][0] = 'WEST'
		self.assertEqual(robot(commands), output_table)
	def test_rotate_WEST_RIGHT(self):
		commands = [
			'PLACE 0,0,WEST',
			'RIGHT'
		]
		output_table = get_clear_table()
		output_table[0][0] = 'NORTH'
		self.assertEqual(robot(commands), output_table)
	def test_sequence_of_3_commands(self):
		commands = [
			'PLACE 0,0,NORTH',
			'MOVE',
			'MOVE'
		]
		output_table = get_clear_table()
		# output_table[0][0] = 'NORTH'
		# output_table[0][1] = 'NORTH'
		output_table[0][2] = 'NORTH'
		self.assertEqual(robot(commands), output_table)
	def test_sequence_of_MOVEs(self):
		commands = [
			'PLACE 0,0,NORTH',
			'MOVE',
			'MOVE',
			'MOVE',
			'MOVE',
			'MOVE'
		]
		output_table = get_clear_table()
		# output_table[0][0] = 'NORTH'
		# output_table[0][1] = 'NORTH' move1
		# output_table[0][2] = 'NORTH' move2
		# output_table[0][3] = 'NORTH' move3
		output_table[0][4] = 'NORTH' # move4 stops on y = 4
		# output_table[0][5] = 'NORTH' move5
		self.assertEqual(robot(commands), output_table)
	def test_sequence_PLACE_LEFT_MOVE(self):
		commands = [
			'PLACE 0,0,NORTH',
			'LEFT',
			'MOVE'
		]
		output_table = get_clear_table()
		# output_table[0][0] = 'NORTH'
		# output_table[0][0] = 'WEST'
		output_table[0][0] = 'WEST' #can't do MOVE it
		self.assertEqual(robot(commands), output_table)
	def test_go_to_4_4(self):
		commands = [
			'PLACE 0,0,NORTH',
			'MOVE',
			'MOVE',
			'MOVE',
			'MOVE',
			'MOVE',
			'RIGHT',
			'MOVE',
			'MOVE',
			'MOVE',
			'MOVE'
		]
		output_table = get_clear_table()
		# output_table[0][0] = 'NORTH'
		# output_table[0][1] = 'NORTH' move1
		# output_table[0][2] = 'NORTH' move2
		# output_table[0][3] = 'NORTH' move3
		# output_table[0][4] = 'NORTH' # move4 stops on y = 4
			# output_table[0][5] = 'NORTH' move5 IGNORED
		# output_table[0][4] = 'EAST'
		# output_table[1][4] = 'EAST' move1
		# output_table[2][4] = 'EAST' move2
		# output_table[3][4] = 'EAST' move3
		output_table[4][4] = 'EAST'# move4
		self.assertEqual(robot(commands), output_table)
	def test_go_to_4_4_NORTH(self):
		commands = [
			'PLACE 4,4,NORTH'
		]
		output_table = get_clear_table()
		output_table[4][4] = 'NORTH'
		self.assertEqual(robot(commands), output_table)
	def test_go_to_4_4_NORTH_negative(self):
		commands = [
			'PLACE -4,-4,NORTH'
		]
		output_table = get_clear_table()
		self.assertEqual(robot(commands), output_table)

class TestRobotMethods(unittest.TestCase):
	def test_get_clear_table(self):
		table = [
			['','','','',''],
			['','','','',''],
			['','','','',''],
			['','','','',''],
			['','','','',''],
		]
		self.assertEqual(get_clear_table(), table)

	def test_parse_command_PLACE_1(self):
		command = 'PLACE 4,4,NORTH'
		parsed_command = {
			'PLACE': {
				'place_x': 4,
				'place_y': 4,
				'place_f': 'NORTH'
			},
			'MOVE': False,
			'LEFT': False,
			'RIGHT': False,
			'REPORT': False
		}
		self.assertEqual(parse_command(command), parsed_command)
	def test_parse_command_PLACE_2(self):
		command = 'PLACE 3,4,SOUTH'
		parsed_command = {
			'PLACE': {
				'place_x': 3,
				'place_y': 4,
				'place_f': 'SOUTH'
			},
			'MOVE': False,
			'LEFT': False,
			'RIGHT': False,
			'REPORT': False
		}
		self.assertEqual(parse_command(command), parsed_command)
	def test_parse_command_PLACE_2(self):
		command = 'PLACE 3,4,NABOO'
		parsed_command = {
			'PLACE': False,
			'MOVE': False,
			'LEFT': False,
			'RIGHT': False,
			'REPORT': False
		}
		self.assertEqual(parse_command(command), parsed_command)
	def test_parse_command_MOVE(self):
		command = 'MOVE'
		parsed_command = {
			'PLACE': False,
			'MOVE': True,
			'LEFT': False,
			'RIGHT': False,
			'REPORT': False
		}
		self.assertEqual(parse_command(command), parsed_command)
	def test_parse_command_LEFT(self):
		command = 'LEFT'
		parsed_command = {
			'PLACE': False,
			'MOVE': False,
			'LEFT': True,
			'RIGHT': False,
			'REPORT': False
		}
		self.assertEqual(parse_command(command), parsed_command)
	def test_parse_command_RIGHT(self):
		command = 'RIGHT'
		parsed_command = {
			'PLACE': False,
			'MOVE': False,
			'LEFT': False,
			'RIGHT': True,
			'REPORT': False
		}
		self.assertEqual(parse_command(command), parsed_command)
	def test_parse_command_REPORT(self):
		command = 'REPORT'
		parsed_command = {
			'PLACE': False,
			'MOVE': False,
			'LEFT': False,
			'RIGHT': False,
			'REPORT': True
		}
		self.assertEqual(parse_command(command), parsed_command)

	def test_parse_check_bound(self):
		current_pos_axis = 0
		axis_bound = 4
		increment = 1
		self.assertEqual(check_bound(current_pos_axis, axis_bound, increment), True)
	def test_parse_check_bound(self):
		current_pos_axis = 4
		axis_bound = 4
		increment = 1
		self.assertEqual(check_bound(current_pos_axis, axis_bound, increment), False)



unittest.main()