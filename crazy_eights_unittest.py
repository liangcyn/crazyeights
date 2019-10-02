import crazy_eights
import card_actions

import unittest
import unittest.mock

from card import Card
from game import Game
from unittest.mock import patch
from parameterized import parameterized


class TestCrazyEights(unittest.TestCase):

    @patch('builtins.input', return_value='foo')
    def test_name_prompt_single_player(self, mock_input):
        assert crazy_eights.name_prompt(1, []) == 'foo'

    @patch('builtins.input', return_value='bar')
    def test_name_prompt_multi_player(self, mock_input):
        assert crazy_eights.name_prompt(2, ['foo']) == 'bar'


class TestGameFunctions(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestGameFunctions, self).__init__(*args, **kwargs)
        self.names_list = ['1', '2', '3']
        self.test_game = Game(self.names_list)
        self.test_game.hands = {'1': [Card('queen', 'hearts'), Card('jack', 'spades')],
                                '2': [Card('5', 'hearts')],
                                '3': [Card('10', 'clubs')]}
        self.test_game.pile = [Card('jack', 'clubs')]

    @parameterized.expand([
        (['1'], '1'),
        (['1', '3'], '1 and 3'),
        (['1', '2', '3'], '1, 2, and 3'),
    ])
    def test_create_winner_string(self, winner_list, winner_string):
        assert self.test_game.create_winner_string(winner_list) == winner_string

    def test_get_winners(self):

        winner_list = ['2', '3']
        assert self.test_game.get_winners() == winner_list

    @patch('draw.draw_player_header')
    @patch('draw.draw_deck_and_pile')
    @patch('draw.draw_hand_cards')
    @patch('game.Game.take_a_card')
    @patch('game.Game.query_card_choice')
    @patch('game.Game.play_card')
    @patch('game.Game.play_turn_again')
    @patch('os.system')
    @patch('builtins.input', return_value='\n')
    def test_play_turn(self, mock_input, mock_os, mock_play_turn_again,
                       mock_play, mock_query, mock_take_card,
                       mock_draw_hand, mock_draw_deck, mock_player_header):

        answers = [
            ('1', True),
            ('2', False),
            ('3', True),
        ]

        for player, result in answers:
            hand = self.test_game.hands[player]
            if result:
                assert self.test_game.play_turn(player, hand) == result
            else:
                print(self.test_game.play_turn(player, hand))
                mock_play_turn_again.assert_called_with(player, hand)


class TestCardActions(unittest.TestCase):

    def create_deck(self):

        expected_deck = [Card('value_1', 'suit_1'),
                         Card('value_1', 'suit_2'),
                         Card('value_1', 'suit_3'),
                         Card('value_2', 'suit_1'),
                         Card('value_2', 'suit_2'),
                         Card('value_2', 'suit_3'),
                         Card('value_3', 'suit_1'),
                         Card('value_3', 'suit_2'),
                         Card('value_3', 'suit_3'),
                        ]

        with patch.object(card_actions, 'values',
                          ['value_1', 'value_2', 'value_3']):
            with patch.object(card_actions, 'suits',
                              ['suit_1', 'suit_2', 'suit_3']):
                assert card_actions.create_deck() == expected_deck


if __name__ == '__main__':
    unittest.main()