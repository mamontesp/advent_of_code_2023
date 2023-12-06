def get_instructions(almanac):
	instructions = []
	instruction = []
	for line in almanac:
		if line == '\n':
			instructions.append(instruction)
			instruction = []
		else:
			instruction.append(line.strip())
	instructions.append(instruction)
	return instructions

def create_maps(instruction: list):
	mapped_instruction = [instruction[0].strip(' map:'), sorted([[int(number) for number in line.split()] for line in instruction[1:]], key = lambda x: x[1])]
	return mapped_instruction

def get_source_to_destination(sources: list, list_source_to_destination: list):
	dict_source_to_destination = {}
	for source in sources:
		#print(f'source {source}')
		dict_source_to_destination[source] = source
		for item in list_source_to_destination:
			#print(f'item {item}')
			if source >= item[1] and source <= (item[1] + item[2]):
				soil = source  - item[1] + item[0]
				dict_source_to_destination[source] = soil
				break
	return dict_source_to_destination

def get_seeds_mapping(seeds: list, seed_to_soil_mapping: list):
	print(f'seed_to_soil_mapping {seed_to_soil_mapping}')
	
	seed_ranges = sorted([ seeds[index:index+2] for index in range(0, len(seeds), 2)], key = lambda x: x[0])
	seed_mapping = []
	for seed_range in seed_ranges:
		print(f'seed_range {seed_range}')
		start_seed = seed_range[0]
		end_seed = seed_range[0] + seed_range[1]
		
		for seed_soil in seed_to_soil_mapping:
			if start_seed >= seed_soil[1]:
				if end_seed <= seed_soil[1] + seed_soil[2]:
					seed_mapping.append([start_seed, start_seed, seed_range[1]])
				else:
					seed_mapping.append([start_seed, start_seed, (start_seed - seed_soil[1] + seed_soil[2])])
					start_seed = seed_soil[1] + seed_soil[2] + 1
	print (f'seed_mapping {seed_mapping}')		
	seeds = [item[0] for item in seed_ranges]
	return seed_ranges, seeds


def part_1(seeds, mapped_instructions):
	print(f'seeds {seeds}')
	#print(f"seed-to-soil {mapped_instructions['seed-to-soil']}")
	#print(f"keys {mapped_instructions.keys()}")
	#dict_seed_to_soil = get_seed_to_soil([79, 14, 55, 13], [[50, 98, 2], [52, 50, 48]])
	dict_seed_to_soil = get_source_to_destination(seeds, mapped_instructions['seed-to-soil'])
	dict_soil_to_fertalizer = get_source_to_destination(dict_seed_to_soil.values(), mapped_instructions['soil-to-fertilizer'])
	dict_fertilizer_to_water = get_source_to_destination(dict_soil_to_fertalizer.values(), mapped_instructions['fertilizer-to-water'])
	dict_water_to_light = get_source_to_destination(dict_fertilizer_to_water.values(), mapped_instructions['water-to-light'])	
	dict_light_to_temperature = get_source_to_destination(dict_water_to_light.values(), mapped_instructions['light-to-temperature'])
	dict_temperature_to_humidity = get_source_to_destination(dict_light_to_temperature.values(), mapped_instructions['temperature-to-humidity'])
	dict_humidity_to_location = get_source_to_destination(dict_temperature_to_humidity.values(), mapped_instructions['humidity-to-location'])
	#print(f'dict_seed_to_soil {dict_seed_to_soil}')
	#print(f'dict_soil_to_fertalizer {dict_soil_to_fertalizer}')
	#print(f'dict_fertilizer_to_water {dict_fertilizer_to_water}')
	#print(f'dict_water_to_light {dict_water_to_light}')
	#print(f'dict_light_to_temperature {dict_light_to_temperature}')
	#print(f'dict_temperature_to_humidity {dict_temperature_to_humidity}')
	#print(f'dict_humidity_to_location {dict_humidity_to_location}')
	print (f'min() {min(dict_humidity_to_location.values())}')

def part_2(seeds, mapped_instructions):
	print(f'seeds {seeds}')
	#print(f"seed-to-soil {mapped_instructions['seed-to-soil']}")
	print(f"keys {mapped_instructions.keys()}")
	#dict_seed_to_soil = get_seed_to_soil([79, 14, 55, 13], [[50, 98, 2], [52, 50, 48]])

	dict_seed_to_seed = get_source_to_destination(seeds, mapped_instructions['seed-to-seed'])
	dict_seed_to_soil = get_source_to_destination(dict_seed_to_seed.values(), mapped_instructions['seed-to-soil'])
	dict_soil_to_fertalizer = get_source_to_destination(dict_seed_to_soil.values(), mapped_instructions['soil-to-fertilizer'])
	dict_fertilizer_to_water = get_source_to_destination(dict_soil_to_fertalizer.values(), mapped_instructions['fertilizer-to-water'])
	dict_water_to_light = get_source_to_destination(dict_fertilizer_to_water.values(), mapped_instructions['water-to-light'])	
	dict_light_to_temperature = get_source_to_destination(dict_water_to_light.values(), mapped_instructions['light-to-temperature'])
	dict_temperature_to_humidity = get_source_to_destination(dict_light_to_temperature.values(), mapped_instructions['temperature-to-humidity'])
	dict_humidity_to_location = get_source_to_destination(dict_temperature_to_humidity.values(), mapped_instructions['humidity-to-location'])
	print(f'dict_seed_to_seed {dict_seed_to_seed}')
	#print(f'dict_seed_to_soil {dict_seed_to_soil}')
	#print(f'dict_soil_to_fertalizer {dict_soil_to_fertalizer}')
	#print(f'dict_fertilizer_to_water {dict_fertilizer_to_water}')
	#print(f'dict_water_to_light {dict_water_to_light}')
	#print(f'dict_light_to_temperature {dict_light_to_temperature}')
	#print(f'dict_temperature_to_humidity {dict_temperature_to_humidity}')
	#print(f'dict_humidity_to_location {dict_humidity_to_location}')
	print (f'min() {min(dict_humidity_to_location.values())}')

if __name__ == '__main__':
	#file = open("5_day_input.txt", 'r')
	file = open("5_test_input.txt", 'r')
	with file:
		almanac = file.readlines()
		instructions = get_instructions(almanac)
		seeds = [int(seed) for seed in instructions[0][0].strip('seeds: ').split(' ')]
		mapped_instructions = dict(map(create_maps, instructions[1:]))
		part_1(seeds, mapped_instructions)


		### part 2

		#seeds_mapping, seeds = get_seeds_mapping(seeds, mapped_instructions['seed-to-soil'])
		#print (f'seeds {seeds}')
		#mapped_instructions ['seed-to-seed'] = seeds_mapping
		#part_2(seeds, mapped_instructions)