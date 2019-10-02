import draw
import random

from card import Card


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
	"""
	Creates two ordered lists from cards of its suits and values.

	Parameters:
	cards: a list of Card objects.

	Returns:
	a tuple of a corresponding lists of the cards' suits and values.
	"""
	suits = []
	values = []

	for card in cards:
		suits.append(card.suit)
		values.append(card.value)

	return suits, values
	