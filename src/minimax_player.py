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
        _, move = self.best_outcome_move(board, self.field, True, depth)
        return move

    def best_outcome_move(self, board, our_field, maximize, depth):
        other_field = board.other(our_field)

        best_move = None
        best_outcome = -1
        for move in board.valid_moves(our_field):
            after_move = board.play(move, our_field)
            outcome = None
            if depth == 1:
                outcome = board.my_outcome(our_field)
            else:
                outcome, _ = self.best_outcome_move(after_move, other_field,
                                                    not maximize, depth - 1)
            more = outcome > best_outcome
            less = outcome < best_outcome
            better = (maximize and more) or (not maximize and less)
            if better or best_move is None:
                best_outcome = outcome
                best_move = move

        return best_outcome, best_move
