def predict_next_reading(readings: list):
	list_differences = []
	list_differences.append(readings)
	current_line = readings 
	while True:
		differences = []
		for index in range(1, len(current_line)):
			differences.append(current_line[index] - current_line[ index -1 ])
		list_differences.append(differences)
		current_line = differences
		if all(reading == 0 for reading in current_line):
			differences.append(0)
			break

	for index in range(len(list_differences)-1, 0, -1):
		number_to_append = list_differences[index][-1] + list_differences[index-1][-1] 
		list_differences[index - 1].append(number_to_append)

	print(f'list_differences {list_differences}')
	return list_differences[0][-1]


def get_formatted_sensor_readings(line: str):
	return [int(reading) for reading in line.split()]

def part1(formatted_sensor_readings):
	sensor_readings_with_predictions = list(map(predict_next_reading, formatted_sensor_readings))
	sum_predictions = sum(sensor_readings_with_predictions)
	#print(f'sensor_readings_with_predictions {sensor_readings_with_predictions}')
	print(f'sum predictions part 1 {sum_predictions}')


def part2(formatted_sensor_readings):
	reversed_formatted_sensor_readings = [formatted_sensor_reading[::-1] for formatted_sensor_reading in formatted_sensor_readings]
	sensor_readings_with_predictions = list(map(predict_next_reading, reversed_formatted_sensor_readings))
	sum_predictions = sum(sensor_readings_with_predictions)
	#print(f'sensor_readings_with_predictions {sensor_readings_with_predictions}')
	print(f'sum predictions part 2 {sum_predictions}')
	

if __name__ == '__main__':
	file = open("9_day_input.txt", 'r')
	#file = open("9_test_input.txt", 'r')
	with file:
		sensor_readings = file.readlines()
		formatted_sensor_readings = list(map(get_formatted_sensor_readings,sensor_readings))
		
		part1(formatted_sensor_readings)
		part2(formatted_sensor_readings)

		

