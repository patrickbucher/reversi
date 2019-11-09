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

    def test_illegal_moves(self):
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
        board = Board.from_fields(fields)
        illegal_moves = {
            board.FIELD_BLACK: [(0, 7), (6, 2), (6, 6)],
            board.FIELD_WHITE: [(0, 0), (2, 3), (2, 5)]
        }

        for (color, moves) in illegal_moves.items():
            for move in moves:
                try:
                    board.play(move, color)
                except ValueError:
                    pass
                else:
                    self.fail('{} move {} applied'.format(color, move))

    def test_perform_black_move(self):
        initial = np.asarray([
            [0, 0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0],
            [1, 1, 1, 1, 2, 0, 0, 0],
            [0, 0, 0, 1, 2, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ])
        move = (3, 5)
        outcome = np.asarray([
            [0, 0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ])

        board = Board.from_fields(initial)
        board = board.play(move, board.FIELD_BLACK)

        self.assertTrue(np.array_equal(board.fields, outcome))

    def test_perform_white_move(self):
        initial = np.asarray([
            [0, 0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0],
            [1, 1, 1, 1, 2, 0, 0, 0],
            [0, 0, 0, 1, 2, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ])
        move = (4, 2)
        outcome = np.asarray([
            [0, 0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0],
            [1, 1, 1, 2, 2, 0, 0, 0],
            [0, 0, 2, 2, 2, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ])

        board = Board.from_fields(initial)
        board = board.play(move, board.FIELD_WHITE)

        self.assertTrue(np.array_equal(board.fields, outcome))

    def test_big_fictional_move(self):
        initial = np.asarray([
            [2, 2, 2, 2, 2, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 1, 1, 0, 1, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 2, 2, 2, 2, 2]
        ])
        move = (3, 4)
        outcome = np.asarray([
            [2, 2, 2, 2, 2, 2, 2, 2],
            [2, 1, 2, 1, 2, 1, 2, 2],
            [2, 1, 1, 2, 2, 2, 1, 2],
            [2, 2, 2, 2, 2, 2, 2, 2],
            [2, 1, 1, 2, 2, 2, 1, 2],
            [2, 1, 2, 1, 2, 1, 2, 2],
            [2, 2, 1, 1, 2, 1, 1, 2],
            [2, 2, 2, 2, 2, 2, 2, 2]
        ])

        board = Board.from_fields(initial)
        board = board.play(move, board.FIELD_WHITE)

        self.assertTrue(np.array_equal(board.fields, outcome))

    def test_outcome_initial_position(self):
        initial = np.asarray([
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 1, 0, 0, 0],
            [0, 0, 0, 1, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ])
        board = Board.from_fields(initial)
        expected_finished = False
        expected_black = 2
        expected_white = 2

        finished, black, white = board.outcome()

        self.assertEqual(finished, expected_finished)
        self.assertEqual(black, expected_black)
        self.assertEqual(white, expected_white)

    def test_outcome_final_position(self):
        position = np.asarray([
            [2, 2, 2, 2, 2, 2, 2, 2],
            [2, 1, 2, 1, 2, 1, 2, 2],
            [2, 1, 1, 2, 2, 2, 1, 2],
            [2, 2, 2, 2, 2, 2, 2, 2],
            [2, 1, 1, 2, 2, 2, 1, 2],
            [2, 1, 2, 1, 2, 1, 2, 2],
            [2, 2, 1, 1, 2, 1, 1, 2],
            [2, 2, 2, 2, 2, 2, 2, 2]
        ])
        board = Board.from_fields(position)
        expected_finished = True
        expected_black = 16
        expected_white = 48

        finished, black, white = board.outcome()

        self.assertEqual(finished, expected_finished)
        self.assertEqual(black, expected_black)
        self.assertEqual(white, expected_white)

    def test_render(self):
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
        board = Board.from_fields(fields)
        expected_rendering = """
  1 2 3 4 5 6 7 8
a - - - - - - - -
b - - - - - - - -
c - - - - - - - -
d - - - o x - - -
e - - - x o - - -
f - - - - - - - -
g - - - - - - - -
h - - - - - - - -
        """.strip()

        rows = [chr(c + ord('a')) for c in range(8)]
        cols = [chr(c + ord('0')) for c in range(1, 9)]
        rendering = board.render('-', 'x', 'o', rows, cols)

        self.assertEqual(rendering, expected_rendering)


if __name__ == '__main__':
    unittest.main()
