def get_formatted_lever(line: str):
	return list(line.strip())

def get_rock_positions(line: list):
	return [x[0] for x in list(filter(lambda x: x[1] == 'O', enumerate(line)))]

def get_square_positions(line: list):
	return [x[0] for x in list(filter(lambda x: x[1] == '#', enumerate(line)))]

def get_next_valid_position(square_positions: list, rock_position: int):
	print (f'square_positions {square_positions}')
	print (f'rock_position {rock_position}')
	position = 0
	for square_position in square_positions[::-1]:
		if rock_position > square_position:
			position = square_position + 1 
			break
	print (f'first position {position}')	
	return position


def get_tilted_lever(lever: list):
	transposed_lever = [[lever[column][row] for column in range(len(lever[0]))] for row in range(len(lever))]

	print('transposed_lever')
	for line in transposed_lever:
		print(line)
	for row, line in enumerate(transposed_lever):
		rock_positions = get_rock_positions(line)
		square_positions = get_square_positions(line)

		default_rock_positions = ['O'] * len(rock_positions)
		new_rock_positions = {}
		for rock_position in rock_positions:
			






















		#print (f'rock_positions {rock_positions}')
		#print (f'square_positions {square_positions}')
		if not rock_positions:
			print ('skip')
			continue
		aux_column = 0
		counter = 0
		print(f'row {row}-------')
		if square_positions:
			aux_column = get_next_valid_position(square_positions, rock_positions[0])

		square_index = 0
		for column, rock_position in enumerate(rock_positions):
			if square_positions:
				square_index += 1
				aux_column = get_next_valid_position(square_positions, rock_position)

			aux_column += counter
			if transposed_lever[row][aux_column] != '#':
			   transposed_lever[row][aux_column] = 'O'
			   if rock_position > aux_column:
			   		transposed_lever[row][rock_position] = '.' 
			else:
				print('new #')				
			counter += 1
			
	
	tilted_lever = [[transposed_lever[column][row] for column in range(len(transposed_lever[0]))] for row in range(len(transposed_lever))]
	
	print('transposed_lever')
	#for line in transposed_lever:
		#print(line)

	print('tilted_lever')
	for line in tilted_lever:
		print(line)

	return tilted_lever


def get_load_per_line(line: list):
	return line[1].count('O') * line[0]

if __name__ == '__main__':
	#file = open("14_day_input.txt", 'r')
	file = open("14_test_input.txt", 'r')
	lever_lines = file.readlines()
	formatted_lever = list(map(get_formatted_lever, lever_lines))
	
	print('formatted_lever')
	for line in formatted_lever:
		print(line)
	tilted_lever = get_tilted_lever(formatted_lever)

	scored_tilted_lever = list(zip(range(len(tilted_lever), 0, -1), tilted_lever))
	for line in scored_tilted_lever:
		print(line)

	load = list(map(get_load_per_line, scored_tilted_lever))
	print(f'sum load {sum(load)}')






