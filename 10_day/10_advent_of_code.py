START = 'S'

moves = {
		 'S': [(0, -1), (-1, 0), (0, 1), (1, 0)],
		 '|': [(1, 0), (-1, 0)],
		 '-': [(0, 1), (0, -1)], 
		 'L': [(-1, 0),(0, 1)], 
		 'J': [(0, -1),(-1, 0)],
		 '7': [(1, 0),(0, -1)],
		 'F': [(1, 0),(0, 1)]
		 #'.': [{0,0}]
		}
				  
rules = {(0, -1): ['-', 'F', '7'], #ok
		 (-1, 0): ['|', 'F', 'L'],
		 (0, 1):['-', 'J', '7'],
		 (1, 0): ['|', 'L', 'J'] #ok
		 }

def get_start_position(maze_lines: list):
	position = ()
	for index, maze_line in enumerate(maze_lines):
		#print(f'maze_line {maze_line}')
		if START in maze_line:
			position = (index, maze_line.index(START))
			break
	return position

def get_opposite_tuple(tuple_coor: tuple):
	return (tuple_coor[0]*-1, tuple_coor[1]*-1)

maze = {}
def get_maze_as_graph(maze_lines: list, start_position: tuple, last_move: tuple):
	current_position = start_position
	current_symbol = maze_lines[current_position[0]][current_position[1]]
	if current_position in maze:
		return 0

	maze[current_position] = set()
	
	possible_moves = moves[current_symbol].copy()
	if last_move in possible_moves:
		print(f'removing last move {last_move}')
		possible_moves.remove(last_move)
	print(f'current_position {current_position}  move {current_symbol} possible_moves {possible_moves}')
	
	for coor in possible_moves:
		print(f'coor {coor}')
		new_position = (current_position[0]+coor[0], current_position[1] + coor[1])

		print(f'new_position {new_position} move {maze_lines[new_position[0]][new_position[1]]} expected_moves {rules[coor]}')
		if maze_lines[new_position[0]][new_position[1]] in rules[coor]:
			maze[current_position].add(new_position)
			print('YES')
			get_maze_as_graph(maze_lines, new_position, get_opposite_tuple(coor))
		print('NO')


def get_formatted_maze(maze_line: list):
	return list(maze_line.strip())

if __name__ == '__main__':
	#file = open("10_day_input.txt", 'r')
	file = open("10_test_input_2.txt", 'r')
	with file:
		maze_lines = file.readlines()
		formatted_maze = list(map(get_formatted_maze, maze_lines))
		start_position = get_start_position(formatted_maze)
		print(f'start_position {start_position}')
		get_maze_as_graph(formatted_maze, start_position, (0, 0))
		print(maze)
