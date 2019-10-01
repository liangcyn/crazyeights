from game import Game
import draw
import os

def crazy_eights():
	startup_prompt()


def startup_prompt():
	"""
	Lists rules upon startup, prompts game.
	"""
	print()
	draw.draw_centered('WELCOME TO CRAZY EIGHTS!', '-')
	print('a quick rundown of the rules:')

	print('\n\nGAMEPLAY:')
	print('- each player is dealt five cards.')

	print('- players will draw from the remaining deck.')
	print('- the top card of the deck is turned face up to start the discard pile next to it.')

	print('- in order, each player adds to the pile by playing one card,\n such that any of these are true:')

	print('\t- the played card\'s suit matches the top card on the pile')
	print('\t- the played card\'s value matches the top card on the pile')
	print('\t- the played card\'s value is an eight')

	print('- a player who cannot fulfill any of these rules must\n draw cards from the deck until they can play one.')
	print('- till the deck is empty, all players must have 5 cards in their hands.')
	print('- when the draw pile is empty, a player who cannot add to the\n discard pile passes their turn.')

	print('\n\nWIN CONDITIONS:')
	print('- in a single-player game, the player must play all their cards to win.')
	print('- in a multiplayer game, the first player to discard all of their cards,\n',
		'or the players with the lowest amount of cards when there are no possible plays left, wins.')

	print('\n\nthis game can be played with 1-5 players.')
	print('enter the number of players in your game session, or any non-integer key to exit.')

	num_players = num_players_prompt()

	names_list = []

	for player_index in range(num_players):
		names_list.append(name_prompt(player_index + 1, names_list))

	new_game = Game(names_list)
	new_game.init_game()


def num_players_prompt():
	"""
	Prompts user input on how many players are in the current game session.

	Returns:
	number of players if user input fulfills conditions;
	else reprompts or exits.
	"""
	user_input = input()

	try:
		num_players = int(user_input)
	except ValueError:
		print("see you later!")
		exit()

	player_conditions_fulfilled = num_players >= 1 and num_players <= 5

	if not player_conditions_fulfilled:
		print('sorry! we can only have 1-5 players for this game.')
		print('enter the number of players in your game session, or any non-number key to exit.')
		return num_players_prompt()

	return num_players


def name_prompt(player_index, names_list):
	"""
	Prompts users for player names so the program can call players when it is their turn.

	Parameters:
	player_index: int index of the player.
	names_list: list of already-inputted names.

	Returns:
	a string of the unique player name.
	"""
	print("hi, player %i! please enter in a unique name." %player_index)
	player_name = input()
	if player_name in names_list:
		print("we already have a player named %s. please try another name." %player_name)
		name_prompt(player_index, names_list)
	return player_name


if __name__ == '__main__':
	crazy_eights()
