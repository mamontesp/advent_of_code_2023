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
	mask_matrix = [[0 for row in range(len(schematic_matrix[0]))] for column in range(len(schematic_matrix))]
	for symbol_location in symbol_locations_list:
		adjacent_symbol_matrix = get_adjacent_symbol_matrix(symbol_location, schematic_matrix)
		for row_index, row in enumerate(range(symbol_location[0]-1, symbol_location[0]+2)):
			for column_index, column in enumerate(range(symbol_location[1]-1, symbol_location[1]+2)):
				mask_matrix[row][column] = adjacent_symbol_matrix[row_index][column_index]
	return mask_matrix

def get_part_numbers_per_line(line, mask):
	numbers = []
	number = ''
	number_to_append = False
	last_index = len(line) -1 
	for index, (item_line, masked) in enumerate(zip(line, mask)):
		#print (f'item line {item_line}')
		if item_line.isdigit():
			number += item_line
			if masked == 1:
				number_to_append = True
		if index is last_index or not item_line.isdigit():
			if not number_to_append:
				number = ''
			elif number:
				numbers.append(int(number))
				number_to_append = False
				number = ''
	return numbers


def get_part_numbers(schematic_matrix, mask_adjacent_digit_matrix):
	part_numbers = []
	for index_line, line in enumerate(schematic_matrix):
		for number in get_part_numbers_per_line(line, mask_adjacent_digit_matrix[index_line]):
			part_numbers.append(number)
	return  part_numbers


def format_schematic_line(schematic_line: str):
	formatted_schematic_line = schematic_line.strip()
	return formatted_schematic_line

if __name__ == '__main__':
	file = open("3_day_input.txt", 'r')
	with file:
		schematic_lines = file.readlines()
		formatted_schematic_lines = list(map(format_schematic_line, schematic_lines))
		schematic_matrix = [[element for element in line ] for line in formatted_schematic_lines]
		symbol_locations = get_symbol_locations(schematic_matrix)
		mask_adjacent_digit_matrix = get_mask_adjacent_digit_matrix(symbol_locations, schematic_matrix)
		part_numbers = get_part_numbers(schematic_matrix, mask_adjacent_digit_matrix)
		print(f'sum {sum(part_numbers)}')
		