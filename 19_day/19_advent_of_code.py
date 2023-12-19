import re
p = re.compile('([xmsa]{1}[<>]{1}[0-9]+)')

def is_a_valid_condition(rule: str):
	return True if p.match(rule) else False

def eval_condition(rule: str, a = 0, m=0, s=0, x=0):
	#print(f'rule {rule} a={a} m={m} s={s} x={x}')
	result = eval(rule)
	#print(f'result {result}')
	return result

def get_rating_input(rating):
	input = rating.split('=')
	return input[0], int(input[1])


def define_workflows_ratings(file):
	workflows = {}
	rating_parts = []
	blank_line_pass = False

	with file:
		while True:
			line = file.readline().strip()
			if line == '':
				blank_line_pass == True
				break
			if not blank_line_pass: 
				data = line.strip('}').split('{')
				#print (f'workflow {data}')
				rules = list(data[1].split(','))
				conditions = [rule.split(':') for rule in rules]
				workflows[data[0]] = conditions

		while True:
			line = file.readline().strip()
			if line == '':
				break
			else:
				data = line.strip('{}').split(',')
				#print(f'rating {data}')
				dict_rating = dict(map(get_rating_input, data))
				rating_parts.append(dict_rating)
	return workflows, rating_parts

def get_accepted_parts(workflows: list, rating_parts: list, ):
	first_workflow = workflows['in']
	accepted_parts = []

	for part in rating_parts:
		current_worflow = first_workflow
		count = 0
		while True:
			rule = current_worflow[count]
			#print(f'new_rule {rule}')
			is_valid_condition = is_a_valid_condition(rule[0])
			if is_valid_condition:
				#print(f'is_valid_condition {is_valid_condition}')
				if eval_condition(rule[0], **part):
					if rule[1] == 'A':
						accepted_parts.append(part)
						break
					if rule[1] == 'R':
						break
					current_worflow = workflows[rule[1]]
					count = 0
				else:
					count+=1
			else:
				if rule[0] == 'A':
					accepted_parts.append(part)
					break
				if rule[0] == 'R':
					break
				current_worflow = workflows[rule[0]]
				count = 0
			#break
	return accepted_parts


def get_sum_ratings(part: dict):
	sum_part = 0
	for key in part:
		sum_part += part[key]

	return sum_part



if __name__ == '__main__':
	file = open("19_day_input.txt", 'r')
	#file = open("19_test_input.txt", 'r')
	workflows, rating_parts = define_workflows_ratings(file)
	accepted_parts = get_accepted_parts(workflows, rating_parts)
	#print (f'accepted_parts {accepted_parts}')
	list_sum_ratings = list(map(get_sum_ratings, accepted_parts))
	#print(f'list_sum_ratings {list_sum_ratings}')

	sum_accepted_parts_ratings = sum(list_sum_ratings)
	print(f'sum_accepted_parts_ratings {sum_accepted_parts_ratings}')
	
