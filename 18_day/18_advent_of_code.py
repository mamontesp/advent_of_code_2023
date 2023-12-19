coords = {'U': (-1,0),
		  'L': (0, -1),
		  'D': (1, 0),
		  'R': (0, 1)
}

def get_formatted_dig_plan(line: str):
	dig_plan_line = line.strip().split()
	dig_plan_line[1] =  int(dig_plan_line[1])
	dig_plan_line[2] = dig_plan_line[2].strip('(#)')
	return dig_plan_line

def define_zone(dig_plan: list):
	max_rows = 0
	rows = 0
	max_columns = 0
	columns = 0
	for instruction in dig_plan:
		if instruction[0] == 'R':
			columns += instruction[1]
			if columns > max_columns:
				max_columns = columns
			continue
		if instruction[0] == 'L':
			columns -= instruction[1]
			if columns > max_columns:
				max_columns = columns
			continue
			
		if instruction[0] == 'U':
			rows -= instruction[1]
			if rows > max_rows:
				max_rows = rows
			continue
		if instruction[0] == 'D':
			rows += instruction[1]
			if rows > max_rows:
				max_rows = rows
			continue

	return max_rows + 1, max_columns + 1 

def count_dugs(terrain: list):
	counts_per_row = 0
	for row in terrain:
		counts_per_row = row.count('#')
		for dugs in range(0, count_per_row, 2):
			



def define_perimeter(dig_plan: list, zone: tuple):
	base_terrain = [['.' for column in range(zone[1])] for row in range(zone[0])] 
	#print(f'base_terrain {base_terrain}')
	initial_pos = (0, 0)
	current_pos = initial_pos
	for instruction in dig_plan:
		print(f'current_pos {current_pos}')
		base_coord = coords[instruction[0]]
		number_steps = instruction[1]
		#base_terrain[current_pos[0]][current_pos[1]] = '#'
		for step in range(number_steps):
			base_terrain[current_pos[0] + base_coord[0] * step][current_pos[1] + base_coord[1] * step] = '#'
		current_pos = (current_pos[0] + base_coord[0] * number_steps, current_pos[1] + base_coord[1] * number_steps)
		
	return base_terrain

if __name__ == '__main__':
	#file = open("18_day_input.txt", 'r')
	file = open("18_test_input.txt", 'r')
	dig_plan_lines = file.readlines()
	dig_plan_formatted = list(map(get_formatted_dig_plan, dig_plan_lines))
	print (dig_plan_formatted)
	zone = define_zone(dig_plan_formatted)
	print (f'zone {zone}')

	perimeter = define_perimeter(dig_plan_formatted, zone)
	for line in perimeter:
		print(line)