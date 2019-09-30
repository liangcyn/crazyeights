import card_actions
from card_actions import CRAZY_EIGHT, NUM_INITIAL_CARDS_IN_HAND
from card import Card, NUMBER_OF_CARDS
import draw
import os
import random

class Game:
	def __init__(self, names_list):
		self.deck = card_actions.create_deck()
		self.pile = card_actions.create_pile()

		self.num_players = len(names_list)
		self.names_list = names_list
		self.hands = {player_name: [] for player_name in names_list}

		self.possible_plays_exist = [True for player in names_list]

	def init_game(self):
		self.deck = card_actions.shuffle_deck(self.deck)

		# deal cards for each player
		for player, hand in self.hands.items():
			self.deal_hand(player)

		self.play_game()

	def play_game(self):
		# turn over first card on deck
		self.add_to_pile(self.deck.pop(0))

		while self.game_is_active():
			for num, (player, hand) in enumerate(self.hands.items()):
				self.possible_plays_exist[num] = self.play_turn(player, hand)
				if not self.game_is_active:
					break

		self.handle_game_results()

	def get_winners(self):
		num_cards_for_each_player = [len(hand) for player, hand in self.hands.items()]
		min_num_cards = min(num_cards_for_each_player)
		winner_list = [self.names_list[i] for i, num_cards in enumerate(num_cards_for_each_player) if num_cards == min_num_cards]
		return winner_list

	def create_winner_string(self, winner_list):
		winner_string = ''
		last_elem_index = len(winner_list) - 1

		for winner in winner_list[:last_elem_index]:
			winner_string += winner + ', '

		if winner_string:
			winner_string += 'and '

		winner_string += winner_list[last_elem_index]

		return winner_string


	def handle_game_results(self):
		draw.draw_result_bar()
		card_actions.print_game_state(self.hands, self.deck, self.pile)
		# players did not expend all cards into pile

		hands_contain_cards = [hand for player, hand in self.hands.items()]

		# if one-player game, if their hand is not empty, they lose.
		if len(self.hands) <= 1 and self.hands[0] != []:
			draw.draw_centered('YOU LOSE', '')
			print('sorry, you did not play all your cards.')
			print('better luck next time!')
			exit()

		# otherwise, set the winner(s) as the one(s) with the least cards.
		winner_list = self.get_winners()

		winner_string = self.create_winner_string(winner_list)

		draw.draw_centered(' CONGRATS! ', u'\u2b51')
		draw.draw_centered('congratulations, %s! you won!' %winner_string, ' ')
		draw.draw_centered('play again sometime!', ' ')
		exit()
		

	def game_is_active(self):
		# make sure that moves can be made by at least one player.
		moves_are_left = (self.possible_plays_exist != [False] * self.num_players)
		hands_contain_cards = [hand for player, hand in self.hands.items()]
		no_hand_is_empty = [] not in hands_contain_cards
		return moves_are_left and no_hand_is_empty


	def play_turn(self, player, hand):
		os.system('cls' if os.name == 'nt' else 'clear')

		draw.draw_player_header(player)

		last_card_played = self.top_card_on_pile()

		suit_to_match = last_card_played.suit
		value_to_match = last_card_played.value

		draw.draw_deck_and_pile(suit_to_match, value_to_match, self.deck)

		hand_suits, hand_values = card_actions.create_card_lists(hand)
		possible_plays = []

		for card in hand:
			if (card.suit == suit_to_match or
				card.value == value_to_match or
				card.value == CRAZY_EIGHT):
				possible_plays.append(card)

		draw.draw_hand_cards(hand_suits, hand_values)

		if not possible_plays:
			if not self.deck:
				print('you have no possible plays. press enter to continue.')
				ans = input()
				return False
			print("you cannot play any of your current cards. press enter to take another card.")
			ans = input()
			self.take_a_card(player)
			return self.play_turn(player, hand)


		card_index = self.query_card_choice(player, possible_plays)
		self.play_card(player, card_index)

		return True

	def query_card_choice(self, player, possible_plays):
		print('input the index of the card you would like to choose:')

		card_index = -1
		ans = input()
		try:
			card_index = int(ans) - 1
		except ValueError:
			print('please enter a valid integer.')
			return self.query_card_choice(player, possible_plays)

		if card_index < 0 or card_index >= len(self.hands[player]):
			print('not an index of one of your cards.')
			return self.query_card_choice(player, possible_plays)

		potential_card = self.hands[player][card_index]

		if potential_card not in possible_plays:
			print('can\'t play this card! make sure that at least one of the following is true:')
			print('\t- the played card\'s suit matches the top card on the pile')
			print('\t- the played card\'s value matches the top card on the pile')
			print('\t- the played card is a crazy eight!')
			return self.query_card_choice(player, possible_plays)

		return card_index
		

	def play_card(self, player, card_index):
		card_to_play = self.hands[player][card_index]
		print('CARD:', card_to_play.value, 'of', card_to_play.suit)
		self.hands[player].remove(card_to_play)
		self.add_to_pile(card_to_play)

		# if deck still has cards and players have less than
		# the initial amount of cards, they must take a card
		if self.deck and len(self.hands[player]) < NUM_INITIAL_CARDS_IN_HAND:
			self.take_a_card(player)

	def deal_hand(self, player):
		for _ in range(NUM_INITIAL_CARDS_IN_HAND):
			# deck is empty
			if not self.deck:
				return

			self.take_a_card(player)

	def take_a_card(self, player):
		hand = self.hands[player]
		self.hands[player].append(self.deck.pop(0))

	def add_to_pile(self, card):
		self.pile.append(card)

	def top_card_on_pile(self):
		return self.pile[len(self.pile)-1]