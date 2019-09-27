import math

VALUE_SYMBOLS = {'ace': 'A',
				 '2': '2',
				 '3': '3',
				 '4': '4',
				 '5': '5',
				 '6': '6',
				 '7': '7',
				 '8': '8',
				 '9': '9',
				 '10': '10',
				 'jack': 'J',
				 'queen': 'Q',
				 'king': 'K'}

SUIT_SYMBOLS = {'clubs': u'\u2663',
				'diamonds': u'\u2666',
				'hearts': u'\u2665',
				'spades': u'\u2660'}

CARD_WIDTH = 11

NUM_CARDS_DRAWN_PER_ROW = 5


def divide_into_rows(card_list): 
    for i in range(0, len(card_list), NUM_CARDS_DRAWN_PER_ROW):  
        yield card_list[i:i + NUM_CARDS_DRAWN_PER_ROW] 

def join_into_string(string_list):
	return ''.join(string_list)

def draw_deck_and_pile(suit_of_top_pile_card, value_of_top_pile_card, deck):
	# sample output:

	# ----PILE---                                         ----DECK---

	#  ---------                                           ---------	
	# |        ♠|                                         |         |	
	# |         |                                         |         |	
	# |         |                                         |  num    |	
	# |    A    |                                         |  cards  |	
	# |         |                                         |  left   |	
	# |         |                                         |         |	
	#  ---------                                           ---------    	
	#  A/spades

	# draw pile on the left, number of cards left in the deck on the right.

	# the spacer is the space between drawing the pile and the deck.
	# subtract 2 for the existence of the pile and deck.

	WIDTH_BETWEEN_PILE_AND_DECK = NUM_CARDS_DRAWN_PER_ROW - 2
	card_space = join_into_string([' '] * CARD_WIDTH)
	spacer = join_into_string([card_space + '\t'] * WIDTH_BETWEEN_PILE_AND_DECK)

	edge_piece = ' --------- \t'
	center_blank_piece = '|         |\t'

	suit_piece = '|        %s|\t' %SUIT_SYMBOLS[suit_of_top_pile_card]

	value_pile_piece = ('|    10   |\t' if value_of_top_pile_card == '10'
				        else '|    %s    |\t' %VALUE_SYMBOLS[value_of_top_pile_card])

	num_deck_piece = ('|    %s   |\t' %str(len(deck)) if len(deck) >= 10
				       else '|    %s    |\t' %str(len(deck)))

	cards_deck_piece = '|  cards  |\t'
	left_deck_piece = '|  left   |'

	print('----PILE---\t' + spacer + '----DECK---\n')
	print(edge_piece + spacer + edge_piece)
	print(suit_piece + spacer + center_blank_piece)
	print(center_blank_piece + spacer + center_blank_piece)
	print(center_blank_piece + spacer + num_deck_piece)
	print(value_pile_piece + spacer + cards_deck_piece)
	print(center_blank_piece + spacer + left_deck_piece)
	print(center_blank_piece + spacer + center_blank_piece)
	print(edge_piece + spacer + edge_piece)


	# draw_card([suit_to_match], [value_to_match], draw_index = False)

def description_piece(index, list_index, value_list, suit_list):
	real_index = index + (list_index * NUM_CARDS_DRAWN_PER_ROW)
	suit = suit_list[real_index]
	value = value_list[real_index]
	
	description = '%s/%s' %(VALUE_SYMBOLS[value], suit)
	total_padding_length = 11 - len(description)
	padding_left_length = int(total_padding_length // 2)
	padding_right_length = total_padding_length - padding_left_length

	padding_left = join_into_string([' '] * padding_left_length)
	padding_right = join_into_string([' '] * padding_right_length)

	return padding_left + description + padding_right + '\t'

def draw_hand_cards(hand_suits, hand_values):
	print('-----------------------------------HAND-----------------------------------\n')
	draw_card(hand_suits, hand_values, draw_index = True)


def draw_card(suit_list, value_list, draw_index):
	# sample output:

	# ----HAND---

	#  ---------    ---------    ---------    ---------	   ---------	
	# |        ♠|  |        ♣|  |        ♠|  |        ♥|  |        ♥|	
	# |         |  |         |  |         |  |         |  |         |	
	# |         |  |         |  |         |  |         |  |         |	
	# |    A    |  |    8    |  |    7    |  |    K    |  |    A    |	
	# |         |  |         |  |         |  |         |  |         |	
	# |         |  |         |  |         |  |         |  |         |	
	#  ---------    ---------    ---------	  ---------    ---------	
	#     [1]          [2]          [3]          [4]          [5]      	
	#  A/spades  	 8/clubs  	 7/spades     K/hearts     A/hearts  

	total_num_cards = len(suit_list)

	# in order to fit most windows, we will draw NUM_CARDS_DRAWN_PER_ROW cards per row.

	split_suit_list = list(divide_into_rows(suit_list))
	split_value_list = list(divide_into_rows(value_list))

	for list_index in range(math.ceil(total_num_cards / NUM_CARDS_DRAWN_PER_ROW)):
		num_cards = len(split_suit_list[list_index])

		edge = join_into_string([' --------- \t' for _ in range(num_cards)])
		midsection = join_into_string(['|         |\t' for _ in range(num_cards)])
		suit_wedge = join_into_string(['|        %s|\t' %SUIT_SYMBOLS[suit]for suit in split_suit_list[list_index]])
		
		# values needed to be treated slightly differently,
		# as 10 is the only 2-character value and will have alignment issues.
		value_wedge = ''
		for value in split_value_list[list_index]:
			if value == '10':
				value_wedge += '|    10   |\t'
			else:
				value_wedge += '|    %s    |\t' %VALUE_SYMBOLS[value]

		# card indices are 1 shifted for more intuitive play.
		indices = join_into_string(['    [%s]      \t' %str(i + (list_index * NUM_CARDS_DRAWN_PER_ROW) + 1) for i in range(num_cards)]) if draw_index else None

		# suit symbols may be hard to see on certain computers.
		# write out descriptions of cards to help with that
		card_description_wedge = ''

		for index in range(num_cards):
			card_description_wedge += description_piece(index, list_index, value_list, suit_list)


		print(edge)
		print(suit_wedge)
		print(midsection)
		print(midsection)
		print(value_wedge)
		print(midsection)
		print(midsection)
		print(edge)
		if indices:
			print(indices)
		print(card_description_wedge)
		print('\n\n')

