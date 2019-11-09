class StdinPlayer:

    # a..h
    rows = [chr(c + ord('a')) for c in range(8)]

    # 1..8
    cols = [chr(c + ord('0')) for c in range(1, 9)]

    def __init__(self, name, field):
        self.name = name
        self.field = field

    def play(self, board):
        rendering = board.render('-', 'x', 'o', self.rows, self.cols)
        print(rendering)
        valid_moves = board.valid_moves(self.field)
        if len(valid_moves) == 0:
            return None

        move = None
        while move is None:
            try:
                user_input = input('{:s}, your move (row col): '
                                   .format(self.name))
                row_str, col_str = user_input.strip().split(' ')
                move = self.input_to_move(row_str, col_str)
            except ValueError as ve:
                print(ve)

            if move not in valid_moves:
                print('invalid move')
                move = None

        return move

    def input_to_move(self, row_str, col_str):
        row = ord(row_str) - ord('a')  # a..h -> 0..7
        col = int(col_str) - 1         # 1..8 -> 0..7
        return (row, col)
