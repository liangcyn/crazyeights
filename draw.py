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

TAB_WIDTH = 4

### CONSTANT PIECES: pieces that are used for multiple draw sessions ###

edge_piece = ' --------- \t'
center_blank_piece = '|         |\t'
cards_deck_piece = '|  cards  |\t'
left_deck_piece = '|  left   |'


def divide_into_rows(card_list): 
    for i in range(0, len(card_list), NUM_CARDS_DRAWN_PER_ROW):  
        yield card_list[i:i + NUM_CARDS_DRAWN_PER_ROW] 


def join_into_string(string_list):
	return ''.join(string_list)


def draw_player_header(player):
	print()
	print()
	draw_centered('', '*')
	draw_centered('Hi, %s!' %player, ' ')
	draw_centered('', '*')
	print()
	print()

def draw_deck_and_pile(suit_of_top_pile_card, value_of_top_pile_card, deck):
	"""
	Draws pile on the left, number of cards left in the deck on the right.

	sample output:

	----PILE---                                         ----DECK---

	 ---------                                           ---------	
	|        ♠|                                         |         |	
	|         |                                         |         |	
	|         |                                         |  40     |	
	|    A    |                                         |  cards  |	
	|         |                                         |  left   |	
	|         |                                         |         |	
	 ---------                                           ---------    	
	 A/spades

	Parameters:
	suit_of_top_pile_card: string of pile card's suit to draw.
	value_of_top_pile_card: string of pile card's value to draw.
	deck: list of cards in deck.
	"""

	# the spacer is the space between drawing the pile and the deck.
	# subtract 2 for the existence of the pile and deck.
	WIDTH_BETWEEN_PILE_AND_DECK = NUM_CARDS_DRAWN_PER_ROW - 2
	card_space = join_into_string([' '] * CARD_WIDTH)
	spacer = join_into_string([card_space + '\t'] * WIDTH_BETWEEN_PILE_AND_DECK)

	suit_piece = get_suit_piece(suit_of_top_pile_card)

	value_pile_piece = get_value_piece(value_of_top_pile_card)

	num_deck_piece = ('|  %s     |\t' %str(len(deck)) if len(deck) >= 10
				       else '|   %s     |\t' %str(len(deck)))

	description_piece = get_description_piece(value_of_top_pile_card,
											  suit_of_top_pile_card)

	print('----PILE---\t' + spacer + '----DECK---\n')
	print(edge_piece + spacer + edge_piece)
	print(suit_piece + spacer + center_blank_piece)
	print(center_blank_piece + spacer + center_blank_piece)
	print(center_blank_piece + spacer + num_deck_piece)
	print(value_pile_piece + spacer + cards_deck_piece)
	print(center_blank_piece + spacer + left_deck_piece)
	print(center_blank_piece + spacer + center_blank_piece)
	print(edge_piece + spacer + edge_piece)
	print(description_piece)
	print()


def get_value_piece(value):
	if value == '10':
		return '|    10   |\t'
	else:
		return '|    %s    |\t' %VALUE_SYMBOLS[value]


def get_description_piece(value, suit):
	"""
	Returns description of card with padding, e.g. ' A/hearts  '

	Parameters:
	value: string containing value of card
	suit: string containing suit of card
	"""
	description = '%s/%s' %(VALUE_SYMBOLS[value], suit)
	total_padding_length = CARD_WIDTH - len(description)
	padding_left_length = int(total_padding_length // 2)
	padding_right_length = total_padding_length - padding_left_length

	padding_left = join_into_string([' '] * padding_left_length)
	padding_right = join_into_string([' '] * padding_right_length)

	return padding_left + description + padding_right + '\t'


def draw_result_bar():
	draw_centered('', '*')
	draw_centered('RESULTS', '-')
	draw_centered('', '*')
	print()


def draw_centered(text_in_bar, bar_symbol):

	total_padding_length =  (NUM_CARDS_DRAWN_PER_ROW *
							 (CARD_WIDTH + TAB_WIDTH))- len(text_in_bar)

	if total_padding_length < 1:
		print(text_in_bar)
		return

	padding_left_length = int(total_padding_length // 2)
	padding_right_length = total_padding_length - padding_left_length

	padding_left = join_into_string([bar_symbol] * padding_left_length)
	padding_right = join_into_string([bar_symbol] * padding_right_length)

	print(padding_left + text_in_bar + padding_right + '\t')


def draw_hand_cards(hand_suits, hand_values):
	draw_centered('HAND', '-')
	draw_card(hand_suits, hand_values, draw_index = True)


def get_suit_piece(suit):
	return '|        %s|\t' %SUIT_SYMBOLS[suit]


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

		edge = join_into_string([edge_piece for _ in range(num_cards)])
		midsection = join_into_string([center_blank_piece for _ in range(num_cards)])
		suit_wedge = join_into_string([get_suit_piece(suit) for suit in split_suit_list[list_index]])
		
		# values needed to be treated slightly differently,
		# as 10 is the only 2-character value and will have alignment issues.
		value_wedge = ''
		for value in split_value_list[list_index]:
			value_wedge += get_value_piece(value)

		# card indices are 1 shifted for more intuitive play.


		# suit symbols may be hard to see on certain computers.
		# write out descriptions of cards to help with visual clarity.
		card_description_wedge = ''

		for index in range(num_cards):
			real_index = index + (list_index * NUM_CARDS_DRAWN_PER_ROW)
			suit = suit_list[real_index]
			value = value_list[real_index]
			card_description_wedge += get_description_piece(value, suit)

		print(edge)
		print(suit_wedge)
		print(midsection)
		print(midsection)
		print(value_wedge)
		print(midsection)
		print(midsection)
		print(edge)
		if draw_index:
			indices = join_into_string([get_indices(i, list_index) for i in range(num_cards)])
			print(indices)
		print(card_description_wedge)
		print('\n\n')


def get_indices(i, list_index):
	return '    [%s]      \t' %str(i + (list_index * NUM_CARDS_DRAWN_PER_ROW) + 1)
