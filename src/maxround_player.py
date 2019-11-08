from board import Board


class MaxroundPlayer:

    def __init__(self, name, field):
        self.name = name
        self.field = field

    def play(self, board):
        valid_moves = board.valid_moves(self.field)
        if len(valid_moves) == 0:
            return None
        if len(valid_moves) == 1:
            return valid_moves[0]

        before = self.my_outcome(board)
        best_move, best_improvement = None, 0
        for candidate in valid_moves:
            fictional_board = board.play(candidate, self.field)
            after = self.my_outcome(fictional_board)
            improvement = after - before
            if improvement > best_improvement:
                best_move = candidate
                best_improvement = improvement

        return best_move

    def my_outcome(self, board):
        _, black, white = board.outcome()
        my = 0
        if self.field == Board.FIELD_BLACK:
            my = black
        else:
            my = white
        return my
