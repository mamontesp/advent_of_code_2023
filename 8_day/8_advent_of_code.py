RIGHT = 'R'
LEFT = 'L'

def get_next_instruction(instructions: list):
	number_instructions = len(instructions)
	instruction_position = 0
	while True:
		yield instructions[instruction_position % number_instructions]
		instruction_position += 1

def get_number_steps(mappings: dict, instructions: list, transit_node, goal_node = 'ZZZ'):
	steps = 0
	gen_instruction = get_next_instruction(instructions)

	while transit_node != goal_node:
		instruction = next(gen_instruction)
		#print (f'transit node {transit_node} - steps {steps} - instruction {instruction}')
		if instruction == RIGHT:
			transit_node = mappings[transit_node][1]
		elif instruction == LEFT:
			transit_node = mappings[transit_node][0]
		else:
			print('You are doing something wrong')
			break
		steps +=1
	return steps

def get_mapping(line: str):
	mapping_list = line.split(' = ')
	data = mapping_list[0]
	locations = mapping_list[1].strip().strip('()').split(', ')
	right = locations[0]
	left = locations[1]
	return [data, (right, left)]

def part1(mappings: dict, instructions: list):
	steps = get_number_steps(mappings, instructions, 'AAA')
	#print (f'instructions {instructions}')
	#print (f'mappings {mappings}')
	print(f'Part 1 steps {steps}')



def does_ends_with_Z(node: str):
	return True if node.endswith('Z') else False

def valid_end_nodes(end_nodes: list):
	list_validation_ends_with_Z = list(map(does_ends_with_Z, end_nodes))
	return False if False in list_validation_ends_with_Z else True


def get_number_steps_part2(mappings: dict, instructions: list):
	steps = 0
	gen_instruction = get_next_instruction(instructions)
	transit_nodes = [key for key in mappings if key.endswith('A')]
	print(f'transit_nodes {transit_nodes}')
	while not valid_end_nodes(transit_nodes):
		instruction = next(gen_instruction)
		print (f'transit node {transit_nodes} - steps {steps} - instruction {instruction}')
		if instruction == RIGHT:
			transit_nodes = [mappings[transit_node][1] for transit_node in transit_nodes]
		elif instruction == LEFT:
			transit_nodes = [mappings[transit_node][0] for transit_node in transit_nodes]
		else:
			print('You are doing something wrong')
			break
		steps +=1
	return steps



def part2(mappings, instructions):
	steps = get_number_steps_part2(mappings, instructions)
	#print (f'instructions {instructions}')
	#print (f'mappings {mappings}')
	print(f'Part 2 steps {steps}')

if __name__ == '__main__':
	file = open("8_day_input.txt", 'r')
	#file = open("8_test_input.txt", 'r')
	#file = open("8_test_input_2.txt", 'r')
	with file:
		instructions = list(file.readline().strip())
		file.readline()
		map_lines = file.readlines()
		mappings = dict(map(get_mapping, map_lines))
		part1(mappings, instructions)
		part2(mappings, instructions)
		
