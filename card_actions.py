from card import Card
import draw
import random

values = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
suits = ['clubs', 'diamonds', 'hearts', 'spades']
NUM_INITIAL_CARDS_IN_HAND = 5
CRAZY_EIGHT = '8'

def create_deck():
	deck = []
	for value in values:
		for suit in suits:
			new_card = Card(value, suit)
			deck.append(new_card)
	return deck

def create_pile():
	return []

def shuffle_deck(deck):
	random.shuffle(deck)
	return deck

def create_card_lists(cards):
	suits = []
	values = []

	for card in cards:
		suits.append(card.suit)
		values.append(card.value)

	return suits, values

def print_game_state(hands, deck, pile):
	for player, hand in hands.items():
		print('----%s\'s HAND---\n' %player)
		hand_suits, hand_values = create_card_lists(hand)
		
		draw.draw_card(hand_suits, hand_values, draw_index = False)

			# print('\t', card.value, 'of', card.suit)

	print('----CARDS LEFT IN DECK---\n')
	deck_suits, deck_values = create_card_lists(deck)

	draw.draw_card(deck_suits, deck_values, draw_index = False)
	# for card in deck:
		# print('\t', card.value, 'of', card.suit)

	print('----CARDS PLAYED IN PILE---\n')

	pile_suits, pile_values = create_card_lists(pile)

	draw.draw_card(pile_suits, pile_values, draw_index = True)
	# for card in pile:
		# print('\t', card.value, 'of', card.suit)
	