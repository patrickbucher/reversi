# Reversi

Reversi implementation in Python using NumPy for educational purposes (learning
Python, NumPy, and Deep Learning).

## Players

- `EdgePlayer` (`edge_player.py`): Tries to pick corners and edges first.
- `MaxroundPlayer` (`maxround_player.py`): Tries to optimize the number of
  stones turned per round.
- `FirstmovePlayer` (`firstmove_player.py`): Picks the first valid move.
- `RandomPlayer` (`random_player.py`): Picks a random valid move.
- `StdinPlayer` (`stdin_player.py`): You playing on `stdin`.

## Running the Sample Code

- Tournament (`tournament.py`): runs a tournament with `n` rounds and the
  defined players (with every player combination twice in different order to
  prevent first-mover advantages)

    Player                 Games     Won    Lost    Ties    Diff
    ------------------------------------------------------------
    Edgar Edge               150      85      64       1     434
    Max Hardcore             150      80      69       1     717
    Freddy Firstmove         150      70      78       2    -358
    Randy Random             150      61      85       4    -793

- Game (`game.py`): play as `StdinPlayer` against the computer
- Simulation: (`simulation.py`): run a number of simulations of two players
  against each other
