also_digits = {
'twone':21,
'oneight': 18,
'threeight': 38,
'fiveight': 58,
'sevenine': 79,
'eightwo':82,
'eighthree': 83,
'nineight': 98,
'one': 1, 
'two': 2,
'three': 3,
'four': 4,
'five': 5,
'six': 6,
'seven': 7,
'eight': 8,
'nine': 9
}

def map_string_digits(line: str):
	for key, value in also_digits.items():
		line = line.replace(key, str(value))
	return line

file = open("input.txt", 'r')

numbers_list = []
with file:
	lines = file.readlines()
	without_weird_digits_lines = map(map_string_digits, lines)
	for line in without_weird_digits_lines:
		number = ''
		for symbol in line:
			if symbol.isdigit():
				number += symbol
		numbers_list.append(number)

list_result = list(map(lambda x: int(x[0])*10 + int(x[-1]), numbers_list))
print(sum(list_result)) 
print(map_string_digits('fnnineeight1eightninenine8twonejgf'))
#print(list_result[:10])