improve performance
    board.adjacent_of
    board.valid_moves
improve logging
    format
    to file
improve output for stdin player
    use 1..8 as indices
    print indices next to field
    use better indicators than 0, 1, 2 (maybe -, X, O)
implement `edge_player.py`
    from all valid moves
    first pick corners
    then pick edges
    then pick random value
implement `opt_round_player.py`
    iterate over all valid moves
    apply every move
    look what outcome is best
    return this move
implement `minimax_player.py`
    compute full or partial minimax
