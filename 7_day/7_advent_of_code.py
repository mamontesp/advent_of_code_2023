hand_types = dict(zip(['High card','One pair', 'Two pair', 'Three of a kind', 'Full house', 'Four of a kind', 'Five of a kind'], range(1, 8)))

def get_formatted_hands(line: str):
	hand = line.split()
	hand[1] = int(hand[1])
	return hand

def get_hand_type(hand_bid: list):
	#print(f'get_hand_type {hand_bid}')
	hand = hand_bid[0]
	distinct_cards_in_hand = set(hand)	
	counts = []
	has_j = 'J' in hand
	for distinct_card in distinct_cards_in_hand:
		if distinct_card == 'J':
			continue
		counts.append(hand.count(distinct_card))

	if has_j:
		j_count = hand.count('J')
		if j_count != 5:
			max_count = max(counts)
			counts.remove(max_count)
			counts.append(max_count + j_count)
		else: 
			counts.append(5)

	if 5 in counts:
		return [hand_bid[0], hand_bid[1], hand_types['Five of a kind'], 'Five of a kind']
	if 4 in counts:
		return [hand_bid[0], hand_bid[1],  hand_types['Four of a kind'], 'Four of a kind']
	if 3 in counts:
		if 2 in counts:
			return [hand_bid[0], hand_bid[1],  hand_types['Full house'], 'Full house']
		else:
			return [hand_bid[0], hand_bid[1],  hand_types['Three of a kind'],'Three of a kind']
	if 2 in counts:
		counts.remove(2)
		if 2 in counts:
			return [hand_bid[0], hand_bid[1],  hand_types['Two pair'],'Two pair']
		else:
			return [hand_bid[0], hand_bid[1],  hand_types['One pair'], 'One pair']
	else:
		return [hand_bid[0], hand_bid[1],  hand_types['High card'],'High card']


def get_ordered_hands_same_type(hands_same_type: list):
	#print (f'hands_same_type {hands_same_type}')
	#cards_order = ['x','A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
	cards_order = ['x','A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
	ordered_hands = sorted(hands_same_type, key = lambda x: cards_order.index(x[0][0])*(13**4) + cards_order.index(x[0][1])*(13**3)+ cards_order.index(x[0][2])*(13**2) + cards_order.index(x[0][3])*(13**1) + cards_order.index(x[0][4])*(13**0), reverse = True)
	return ordered_hands

def get_ordered_hands(hands: list):
	ordered_hands = sorted(hands, key = lambda x: x[2], reverse = True)
	#print (f'ordered_hands {ordered_hands}')
	hands_by_type_list = [[ordered_hand for ordered_hand in ordered_hands if ordered_hand[2] == hand_types[type]] for type in hand_types]
	ordered_hands_by_type = list(map(get_ordered_hands_same_type, hands_by_type_list))

	ordered_hands_2 = []
	for block in ordered_hands_by_type:
		for hand in block:
			ordered_hands_2.append(hand)

	return list(enumerate(ordered_hands_2))

def get_bids_per_rank(hand: list):
	return (hand[0] + 1) * hand[1][1]

if __name__ == '__main__':
	file = open("7_day_input.txt", 'r')
	#file = open("7_test_input.txt", 'r')
	with file:
		hands = file.readlines()
		formatted_hands = list(map(get_formatted_hands, hands))
		hands_with_types = list(map(get_hand_type, formatted_hands))
		ordered_hands = get_ordered_hands(hands_with_types)
		list_bids_per_rank = list(map(get_bids_per_rank, ordered_hands))
		sum_list_bids_per_rank = sum(list_bids_per_rank)

		#print(f'formatted_hands {formatted_hands}')
		#print(f'hand_types {hands_with_types}')
		#print (f'ordered_hands {ordered_hands}')

		print(f'sum_list_bids_per_rank {sum_list_bids_per_rank}')

