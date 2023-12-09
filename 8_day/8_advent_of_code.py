RIGHT = 'R'
LEFT = 'L'
from math import lcm

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
	print(f'Part 1 steps {steps}')

def does_end_with_Z(node: str):
	return True if node.endswith('Z') else False

def get_steps_return_to_z(node: str, gen_instruction):
	steps = 0
	gen_instruction = get_next_instruction(instructions)
	transit_node = node
	while True:
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
		if does_end_with_Z(transit_node):
			break
	return transit_node, steps

def get_number_steps_part2(mappings: dict, instructions: list):
	transit_nodes = [key for key in mappings if key.endswith('A')]
	steps_by_transit_nodes = []
	print(f'transit_nodes {transit_nodes}')

	for transit_node in transit_nodes:
		steps = 0
		steps_z_to_z = 0
		gen_instruction = get_next_instruction(instructions)
		transit_node, base_steps = get_steps_return_to_z(transit_node, gen_instruction)

		while True:
			new_transit_node, new_steps_z_to_z = get_steps_return_to_z(transit_node, gen_instruction)
			steps += new_steps_z_to_z
			if steps_z_to_z == new_steps_z_to_z:
				break
			steps_z_to_z = new_steps_z_to_z
		steps_by_transit_nodes.append(new_steps_z_to_z)
	return steps_by_transit_nodes


def part2(mappings, instructions):
	steps = get_number_steps_part2(mappings, instructions)
	#print (f'instructions {instructions}')
	#print (f'mappings {mappings}')
	calculated_steps = lcm(*steps)
	print(f'Part 2 steps {steps}')
	print(f'Part 2 calculated_steps  {calculated_steps}')

if __name__ == '__main__':
	file = open("8_day_input.txt", 'r')
	#file = open("8_test_input.txt", 'r')
	#file = open("8_test_input_2.txt", 'r')
	with file:
		instructions = list(file.readline().strip())
		file.readline()
		map_lines = file.readlines()
		mappings = dict(map(get_mapping, map_lines))
		#part1(mappings, instructions)
		part2(mappings, instructions)
		
