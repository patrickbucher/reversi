#!/usr/bin/env python3

import unittest

from edge_player import EdgePlayer


class EdgePlayerTest(unittest.TestCase):

    player = EdgePlayer('Edgy', '1')

    def test_is_corner_negative(self):
        moves = [
            (0, 1),
            (1, 0),
            (1, 1),
            (7, 6),
            (6, 7)
        ]

        for move in moves:
            self.assertFalse(self.player.is_corner(move))

    def test_is_corner_positive(self):
        moves = [
            (0, 0),
            (0, 7),
            (7, 0),
            (7, 7)
        ]

        for move in moves:
            self.assertTrue(self.player.is_corner(move))

    def test_is_edge_negative(self):
        moves = [
            (1, 1),
            (1, 2),
            (3, 4),
            (5, 6),
            (6, 6)
        ]

        for move in moves:
            self.assertFalse(self.player.is_edge(move))

    def test_ist_edge_positive(self):
        moves = [
            (0, 1),
            (0, 2),
            (1, 0),
            (2, 0),
            (7, 1),
            (1, 7),
            (0, 0),
            (7, 7)
        ]

        for move in moves:
            self.assertTrue(self.player.is_edge(move))


if __name__ == '__main__':
    unittest.main()
