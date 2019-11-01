#!/usr/bin/env python3

import unittest

from board import Board

class BoardTest(unittest.TestCase):

    def test_init_empty(self):
        board = Board()
        print(board.fields)

if __name__ == '__main__':
    unittest.main()
