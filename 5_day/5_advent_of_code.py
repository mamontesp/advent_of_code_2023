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
	mapped_instruction = [instruction[0].strip(' map:'), [[int(number) for number in line.split()] for line in instruction[1:]]]
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

def get_seeds_part_2():
	pass

if __name__ == '__main__':
	file = open("5_day_input.txt", 'r')
	with file:
		almanac = file.readlines()
		instructions = get_instructions(almanac)
		seeds = [int(seed) for seed in instructions[0][0].strip('seeds: ').split(' ')]
		mapped_instructions = dict(map(create_maps, instructions[1:]))
		

		print(f'seeds {seeds}')
		print(f"seed-to-soil {mapped_instructions['seed-to-soil']}")
		print(f"keys {mapped_instructions.keys()}")
		#dict_seed_to_soil = get_seed_to_soil([79, 14, 55, 13], [[50, 98, 2], [52, 50, 48]])
		dict_seed_to_soil = get_source_to_destination(seeds, mapped_instructions['seed-to-soil'])
		dict_soil_to_fertalizer = get_source_to_destination(dict_seed_to_soil.values(), mapped_instructions['soil-to-fertilizer'])
		dict_fertilizer_to_water = get_source_to_destination(dict_soil_to_fertalizer.values(), mapped_instructions['fertilizer-to-water'])
		dict_water_to_light = get_source_to_destination(dict_fertilizer_to_water.values(), mapped_instructions['water-to-light'])	
		dict_light_to_temperature = get_source_to_destination(dict_water_to_light.values(), mapped_instructions['light-to-temperature'])
		dict_temperature_to_humidity = get_source_to_destination(dict_light_to_temperature.values(), mapped_instructions['temperature-to-humidity'])
		dict_humidity_to_location = get_source_to_destination(dict_temperature_to_humidity.values(), mapped_instructions['humidity-to-location'])


		print(f'dict_seed_to_soil {dict_seed_to_soil}')
		print(f'dict_soil_to_fertalizer {dict_soil_to_fertalizer}')
		print(f'dict_fertilizer_to_water {dict_fertilizer_to_water}')
		print(f'dict_water_to_light {dict_water_to_light}')
		print(f'dict_light_to_temperature {dict_light_to_temperature}')
		print(f'dict_temperature_to_humidity {dict_temperature_to_humidity}')
		print(f'dict_humidity_to_location {dict_humidity_to_location}')
		print (f'min() {min(dict_humidity_to_location.values())}')





