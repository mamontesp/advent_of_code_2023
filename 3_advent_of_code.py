def is_symbol(element:str):
	return not element.isalnum() and element != '.'

def is_digit(element:str):
	return 1 if element.isdigit() else 0

def get_symbol_locations(schematic_matrix):
	symbol_locations = []
	for line_number, schematic_line in enumerate(schematic_matrix):
		for element_number, element in enumerate(schematic_line):
			if is_symbol(element):
				symbol_locations.append((line_number, element_number))
	return symbol_locations

def get_adjacent_symbol_matrix(location: tuple, schematic_matrix: list):
	#print (f'get_adjacent_symbol_matrix location {location}')
	return [list(map(is_digit, element[location[1]-1:location[1]+2])) for element in schematic_matrix[location[0]-1:location[0]+2]]
	
def get_mask_adjacent_digit_matrix(symbol_locations_list: list, schematic_matrix: list):
	mask_matrix = [[0 for row in range(len(schematic_matrix[0]))] for column in range(len(schematic_matrix)) ]
	#print (f'mask_matrix {mask_matrix}')
	#print (f'mask_matrix index {mask_matrix[0][0]}')
	for symbol_location in symbol_locations_list:
		adjacent_symbol_matrix = get_adjacent_symbol_matrix(symbol_location, schematic_matrix)
		#print (f'adjacent_symbol_matrix {adjacent_symbol_matrix}')
		for row_index, row in enumerate(range(symbol_location[0]-1, symbol_location[0]+2)):
			for column_index, column in enumerate(range(symbol_location[1]-1, symbol_location[1]+2)):
				#print (f'row_index {row_index}, row {row}, column_index {column_index}, column {column}, mask_matrix[row][column] {mask_matrix[row][column]}, adjacent_symbol_matrix[row_index][column_index] {adjacent_symbol_matrix[row_index][column_index]}')
				mask_matrix[row][column] = adjacent_symbol_matrix[row_index][column_index]
				#print(f'adjacent_symbol_matrix {adjacent_symbol_matrix[row_index][column_index]}')
				#print(f'mask_matrix during transform {mask_matrix}')
	print(f'mask_matrix after transform {mask_matrix}')
	return mask_matrix

def format_schematic_line(schematic_line: str):
	formatted_schematic_line = schematic_line.strip()
	return formatted_schematic_line

if __name__ == '__main__':
	file = open("3_day_input.txt", 'r')
	with file:
		schematic_lines = file.readlines()
		formatted_schematic_lines = list(map(format_schematic_line, schematic_lines))
		schematic_matrix = [[element for element in line ] for line in formatted_schematic_lines]
		#print (schematic_matrix)
		#schematic_matrix = [['1', '2', '3'], ['.', '*', '.'], ['7', '8', '9']]
		#print(is_symbol('9'))
		symbol_locations = get_symbol_locations(schematic_matrix)
		print(f'symbol_locations {symbol_locations[0]}')
		print(f'get_adjacent_symbol_matrix {get_adjacent_symbol_matrix(symbol_locations[0], schematic_matrix)}')
		print(get_mask_adjacent_digit_matrix(symbol_locations, schematic_matrix))
		