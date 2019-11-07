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


if __name__ == '__main__':
    unittest.main()
