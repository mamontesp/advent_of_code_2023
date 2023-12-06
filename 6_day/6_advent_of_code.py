def get_races(time_list: list, distance_list: list):
	races = []
	for index, time in enumerate(time_list):
		races.append([int(time), int(distance_list[index])])
	return races


def get_winning_ways(race: list):
	winning_ways = []
	for time_0 in range(race[0]):
		possible_distance = time_0 * race[0] - time_0**2
		if possible_distance >= race[1]:
			winning_ways.append(time_0)
	return len(winning_ways)

def get_mult_winning_ways(winning_ways: list):
	mult = 1
	for ww in winning_ways:
		mult *= ww
	return mult

def part_1(records: list):
	time_list = records[0].strip('Time:\t').strip('\n').split()
	distance_list = records[1].strip('Distance:\t').strip('\n').split()
	print(f'time_list {time_list}')
	print(f'distance_list {distance_list}')

	races = get_races(time_list, distance_list)
	winning_ways = list(map(get_winning_ways, races))
	mult_ww = get_mult_winning_ways(winning_ways)

	print(f'races {races}')
	print(f'winning_ways {winning_ways}')
	print(f'multiplication {mult_ww}')


def part_2(records: list):
	time_list = [int(records[0].strip('Time:\t').strip('\n').replace(' ', ''))]
	distance_list = [int(records[1].strip('Distance:\t').strip('\n').replace(' ', ''))]
	print(f'time_list {time_list}')
	print(f'distance_list {distance_list}')
	races = get_races(time_list, distance_list)
	winning_ways = list(map(get_winning_ways, races))
	mult_ww = get_mult_winning_ways(winning_ways)

	print(f'races {races}')
	print(f'winning_ways {winning_ways}')
	print(f'multiplication {mult_ww}')

if __name__ == '__main__':
	file = open("6_day_input.txt", 'r')
	#file = open("6_test_input.txt", 'r')
	with file:
		records = file.readlines()
		part_1(records)
		part_2(records)
		


