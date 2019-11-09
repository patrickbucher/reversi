class FirstmovePlayer:

    def __init__(self, name, field):
        self.name = name
        self.field = field

    def play(self, board):
        valid_moves = board.valid_moves(self.field)
        if len(valid_moves) == 0:
            return None
        return valid_moves[0]
