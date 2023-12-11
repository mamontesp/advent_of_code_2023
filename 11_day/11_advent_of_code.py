EXPANSION_PART_1 = 2
EXPANSION_PART_2 = 1000000

def get_formatted_universe(universe_line_str: str):
	universe_line = list(universe_line_str.strip())
	return universe_line

def add_cosmic_expansion(formatted_universe: list, expanded_universe: list, expansion):
	#print ('add_cosmic_expansion')
	for index, universe_line in enumerate(formatted_universe):
		list_dots = list(map(lambda x: x == '.', universe_line))
		if all(list_dots):
			expanded_universe[index] = [element * expansion for element in expanded_universe[index]]
		else:
			expanded_universe[index] = [element * 1 for element in expanded_universe[index]]
	
	return expanded_universe

def transpose_universe(universe: list):
	transposed_universe = [[universe[row][column] for row in range(len(universe))] for column in range(len(universe[0]))]
	return transposed_universe

def get_galaxies_locations(universe: list):
	locations = []
	for row, universe_line in enumerate(universe):
		for column, element in enumerate(universe_line):
			if element == '#':
				locations.append((row, column))
	return locations

def get_shortest_path_between_galaxies(galaxies_locations, expanded_universe):
	paths = []
	for index, galaxy_1 in enumerate(galaxies_locations):
		second_index = index + 1
		for galaxy_2 in galaxies_locations[second_index:]:
			row_difference = sum([expanded_universe[row][galaxy_1[1]] for row in range(galaxy_1[0],galaxy_2[0]) ]) #- expanded_universe[galaxy_1[0]][galaxy_1[1]]
			max_column = max(galaxy_1[1],galaxy_2[1])
			min_column = min(galaxy_1[1],galaxy_2[1])
			column_difference = sum([expanded_universe[galaxy_1[0]][column] for column in range(min_column,max_column) ])
			difference = row_difference + column_difference
			paths.append(difference)
			second_index += 1
	return paths


def part1(formatted_universe, expansion):
	expanded_universe = [[1]* len(formatted_universe) for line in formatted_universe]
	#print (f'first_version expanded_universe {expanded_universe}')
	expanded_universe_1 = add_cosmic_expansion(formatted_universe, expanded_universe, expansion)
	transposed_universe = transpose_universe(formatted_universe)
	transposed_expanded_universe = transpose_universe(expanded_universe_1)
	expanded_universe_2 = add_cosmic_expansion(transposed_universe, transposed_expanded_universe, expansion)
	expanded_universe = transpose_universe(expanded_universe_2)
	galaxies_locations = get_galaxies_locations(formatted_universe)
	shortest_paths = get_shortest_path_between_galaxies(galaxies_locations, expanded_universe)

	#print (f'formatted_universe {len(formatted_universe)}')
	#print(f'expanded_universe {len(expanded_universe)}')
	#print(f'galaxies_locations {galaxies_locations}')
	#print(f'shortest_paths {shortest_paths}')
	print(f'sum shortest_paths {sum(shortest_paths)}')

def part2(formatted_universe):
	expanded_universe_1 = add_cosmic_expansion(formatted_universe)
	transposed_universe = transpose_universe(expanded_universe_1)
	expanded_universe_2 = add_cosmic_expansion(transposed_universe)
	expanded_universe = transpose_universe(expanded_universe_2)



if __name__ == '__main__':
	file = open("11_day_input.txt", 'r')
	#file = open("11_test_input.txt", 'r')
	universe_lines = file.readlines()
	formatted_universe = list(map(get_formatted_universe, universe_lines))
	part1(formatted_universe, EXPANSION_PART_1)
	part1(formatted_universe, EXPANSION_PART_2)
	
