from random import choice

from board import Board


class EdgePlayer:

    def __init__(self, name, field):
        self.name = name
        self.field = field

    def play(self, board):
        valid_moves = board.valid_moves(self.field)
        if len(valid_moves) == 0:
            return None
        for move in valid_moves:
            if self.is_corner(move):
                return move
        for move in valid_moves:
            if self.is_edge(move):
                return move
        return choice(valid_moves)

    def is_corner(self, move):
        edge_row = move[0] == 0 or move[0] == (Board.DIM - 1)
        edge_col = move[1] == 0 or move[1] == (Board.DIM - 1)
        return edge_row and edge_col

    def is_edge(self, move):
        edge_row = move[0] == 0 or move[0] == (Board.DIM - 1)
        edge_col = move[1] == 0 or move[1] == (Board.DIM - 1)
        return edge_row or edge_col
