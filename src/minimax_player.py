class MinimaxPlayer:

    DEPTH = 3

    def __init__(self, name, field):
        self.name = name
        self.field = field

    def play(self, board):
        valid_moves = board.valid_moves(self.field)
        if len(valid_moves) == 0:
            return None
        if len(valid_moves) == 1:
            return valid_moves[0]

        moves_left = board.empty_fields()
        depth = min(moves_left, self.DEPTH)
        _, _, move = self.best_outcome_move(board, self.field, depth)
        return move

    def best_outcome_move(self, board, our_field, depth):
        other_field = board.other(our_field)

        my, other = -64, +64
        best_move = None
        best_diff = my - other
        for move in board.valid_moves(our_field):
            after_move = board.play(move, our_field)
            if depth == 1:
                my = board.my_outcome(our_field)
                other = board.my_outcome(other_field)
            else:
                other, my, _ = self.best_outcome_move(after_move, other_field,
                                                      depth - 1)
            diff = my - other
            if diff > best_diff:
                best_diff = diff
                best_move = move

        return my, other, best_move
