#!/usr/bin/env python3

import unittest

import numpy as np

from board import Board


class BoardTest(unittest.TestCase):

    def test_init_empty(self):
        board = Board.start_position()

        white = [[3, 3], [4, 4]]
        black = [[3, 4], [4, 3]]
        empty = [
            [r, c]
            for r in range(0, 8)
            for c in range(0, 8) if r not in [3, 4] or c not in [3, 4]
        ]

        for [r, c] in white:
            self.assertEqual(board.fields[r, c], Board.FIELD_WHITE)

        for [r, c] in black:
            self.assertEqual(board.fields[r, c], Board.FIELD_BLACK)

        for [r, c] in empty:
            self.assertEqual(board.fields[r, c], Board.FIELD_EMPTY)

    def test_init_with_field(self):
        fields = np.zeros((8, 8), dtype=np.uint8)
        board = Board.from_fields(fields)

        for r in range(0, 8):
            for c in range(0, 8):
                self.assertEqual(board.fields[r, c], Board.FIELD_EMPTY)

    def test_valid_initial_moves(self):
        fields = np.asarray([
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 1, 0, 0, 0],
            [0, 0, 0, 1, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ])
        expected_valid_black_moves = [(2, 3), (3, 2), (4, 5), (5, 4)]
        expected_valid_white_moves = [(2, 4), (3, 5), (4, 2), (5, 3)]

        board = Board.from_fields(fields)
        valid_black_moves = board.valid_moves(board.FIELD_BLACK)
        valid_white_moves = board.valid_moves(board.FIELD_WHITE)

        self.assertEqual(valid_black_moves, expected_valid_black_moves)
        self.assertEqual(valid_white_moves, expected_valid_white_moves)

    def test_valid_ingame_moves(self):
        fields = np.asarray([
            [0, 0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0],
            [1, 1, 1, 1, 2, 0, 0, 0],
            [0, 0, 0, 1, 2, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ])
        expected_valid_black_moves = [(1, 5), (2, 3), (2, 5), (3, 5)]
        expected_valid_white_moves = [(2, 2), (4, 2), (4, 6), (5, 2), (5, 6),
                                      (6, 2), (6, 4), (7, 7)]

        board = Board.from_fields(fields)
        valid_black_moves = board.valid_moves(board.FIELD_BLACK)
        valid_white_moves = board.valid_moves(board.FIELD_WHITE)

        self.assertEqual(valid_black_moves, expected_valid_black_moves)
        self.assertEqual(valid_white_moves, expected_valid_white_moves)


if __name__ == '__main__':
    unittest.main()
