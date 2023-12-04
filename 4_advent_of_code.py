def get_formatted_card(card: str):
	formatted_card = card.strip()
	formatted_card = formatted_card.split(': ')
	formatted_card[0] = int(formatted_card[0].strip('Card '))
	formatted_card[1] = [[number for number in numbers.split(' ') if number.isdigit()] for numbers in formatted_card[1].split(' | ')]
	formatted_card.append(1)
	return formatted_card

def get_number_of_points_per_card(card: list):
	intersection = list(set(card[1][0]) & set(card[1][1]))
	if len(intersection) == 0:
		return 0
	return 2**(len(intersection) - 1) 

def get_count_matching_numbers(card:list):
	intersection = list(set(card[1][0]) & set(card[1][1]))
	return len(intersection)

def get_number_of_cards(cards:list):
	list_number_cards = [card[2] for card in cards]
	return sum(list_number_cards)

def accumulate_scratchcards(list_cards: list):
	for card in list_cards:
		matching_cards = get_count_matching_numbers(card)
		if card[0] >= len(list_cards):
			break
		for matching_card in range(matching_cards):
			card_position = card[0] + matching_card
			if card_position >= len(list_cards):
				break
			card_count = card[2]
			list_cards[card_position][2] += card_count
	return list_cards

if __name__ == '__main__':
	file = open("4_day_input.txt", 'r')
	with file:
		cards = file.readlines()
		formatted_list_cards = list(map(get_formatted_card,cards))
		list_points = list(map(get_number_of_points_per_card, formatted_list_cards))
		print(f'sum {sum(list_points)}')
		list_accumulated = accumulate_scratchcards(formatted_list_cards)
		number_of_cards = get_number_of_cards(list_accumulated)
		print(f'count accumulated scratchcards {number_of_cards}')
		
