class StdinPlayer:

    def __init__(self, name, field):
        self.name = name
        self.field = field

    def play(self, board):
        valid_moves = board.valid_moves(self.field)
        if len(valid_moves) == 0:
            return None

        move = None
        while move is None:
            try:
                user_input = input('{:s}, your move (row col): '
                                   .format(self.name))
                row_str, col_str = user_input.strip().split(' ')
                move = (int(row_str), int(col_str))
            except ValueError as ve:
                print(ve)

            if move not in valid_moves:
                print('invalid move')
                move = None

        return move
