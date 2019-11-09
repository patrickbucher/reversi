#!/usr/bin/env python3

import unittest

from stdin_player import StdinPlayer


class StdinPlayerTest(unittest.TestCase):

    def test_input_to_move_topleft(self):
        input_row = 'a'
        input_col = '1'
        expected_move = (0, 0)

        player = StdinPlayer('Player', 1)
        move = player.input_to_move(input_row, input_col)

        self.assertEqual(move, expected_move)

    def test_input_to_move_bottomright(self):
        input_row = 'h'
        input_col = '8'
        expected_move = (7, 7)

        player = StdinPlayer('Player', 1)
        move = player.input_to_move(input_row, input_col)

        self.assertEqual(move, expected_move)


if __name__ == '__main__':
    unittest.main()
