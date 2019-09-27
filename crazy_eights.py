from game import Game
import os

def crazy_eights():
	startup_prompt()


def startup_prompt():
	print('This game can be played with 1-5 players.')
	print('Enter the number of players in your game session, or any non-integer key to exit.')

	num_players = num_players_prompt()

	names_list = []

	for player_index in range(num_players):
		names_list.append(name_prompt(player_index + 1, names_list))

	new_game = Game(names_list)
	new_game.init_game()


def num_players_prompt():
	user_input = input()

	try:
		num_players = int(user_input)
	except ValueError:
		print("See you later!")
		exit()

	player_conditions_fulfilled = num_players >= 1 and num_players <= 5

	if not player_conditions_fulfilled:
		print('Sorry! We can only have 1-5 players for this game.')
		print('Enter the number of players in your game session, or any non-number key to exit.')
		return num_players_prompt()

	return num_players


def name_prompt(player_index, names_list):
	print("Hi, Player %i! Please enter in a unique name." %player_index)
	player_name = input()
	if player_name in names_list:
		print("We already have a player named %s. Please try another name." %player_name)
		name_prompt(player_index, names_list)
	return player_name


if __name__ == '__main__':
	crazy_eights()