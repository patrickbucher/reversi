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
- `MinimaxPlayer` (`minimax_player.py`): Applies Minimax algorithm with maximum depth.

## Running the Sample Code

### Tournament

Tournament (`tournament.py`): runs a tournament with `n` rounds and the defined
players (with every player combination twice in different order to prevent
first-mover advantages).

    Player                 Games     Won    Lost    Ties    Diff
    ------------------------------------------------------------
    Max Minimax               16      13       3       0     392
    Edgar Edge                16      10       6       0     233
    Max Round                 16       8       7       1       2
    Randy Random              16       4      11       1    -296
    Freddy Firstmove          16       4      12       0    -331

### Single Game

Game (`game.py`): play as `StdinPlayer` against the computer.

###  Simulation

Simulation: (`simulation.py`): run a number of simulations of two players
against each other
