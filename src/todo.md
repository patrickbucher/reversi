implement `outcome` function of board, returning scores
    finished: bool, black: int, white: int
implement `game.py`
    constructor requires two players
    until not finished
        m1 = p1.move
        if m1 not is None:
            board = board.play(m1)
        m2 = p2.move
        if m2 not is None:
            board = board.play(m2)
implement players with interface
    move -> returns indices or None if no valid move possible
implement `stdin_player.py`
    get coordinates from stdin
implement `random_player.py`
    get coordinates as random value from valid moves
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
