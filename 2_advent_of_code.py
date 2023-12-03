feasible_cube_output = {
	'red': 12,
	'green': 13,
	'blue':14
}

def format_game(line_game: str):
	formatted_game = line_game.strip()
	formatted_game = formatted_game.split(': ')
	formatted_game[0] = int(formatted_game[0].strip('Game '))
	formatted_game[1] = [[ (cube.split(' ')[1], int(cube.split(' ')[0])) for cube in round.split(', ')] for round in formatted_game[1].split('; ')]
	return formatted_game

def is_a_possible_game(game: list):
	if False in list(map(is_a_possible_set, game[1])):
		return False
	return True

def is_a_possible_set(set_output: list):
	if False in list(map(is_a_possible_cube_output, set_output)):
		return False
	return True

def is_a_possible_cube_output(cube_output: tuple):
	if feasible_cube_output[cube_output[0]] >= int(cube_output[1]):
		return True
	return False

def flatten_set_into_games(game:list):
	#print(f"flatten_set_into_games {game}")
	game[1] = sum(game[1], [])
	return game

def get_max_cube_per_game(game:list, color: str):
	return max(filter(lambda x: x[0] == color, game))

def power_min_set_of_cubes(game: list):
	max_red = get_max_cube_per_game(game[1], 'red')
	max_blue = get_max_cube_per_game(game[1], 'blue')
	max_green = get_max_cube_per_game(game[1], 'green')
	#print(f'game {game} max_red {max_red}, max_blue {max_blue}, max_green {max_green}')
	return max_red[1] * max_blue[1] * max_green[1]

def sum_id_games(formatted_games): 
	valid_games = list(filter(is_a_possible_game, formatted_games))
	return sum([game_index[0] for game_index in valid_games])

def sum_min_set_of_cubes(formatted_games):
	flatten_games = list(map(flatten_set_into_games, formatted_games))
	return sum(list(map(power_min_set_of_cubes, flatten_games)))

if __name__ == '__main__':
	file = open("2_day_input.txt", 'r')
	with file:
		games = file.readlines()
		formatted_games = list(map(format_game, games))
		print(f'Part 1 {sum_id_games(formatted_games)}')
		print(f'Part 2 {sum_min_set_of_cubes(formatted_games)}')


	#print(format_game('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n'))
	