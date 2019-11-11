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
- `CornerMinimaxPlayer` (`cornerminimax_player.py`): First goes for corners, then applies Minimax algorithm.

## Running the Sample Code

### Tournament

Tournament (`tournament.py`): runs a tournament with `n` rounds and the defined
players (with every player combination twice in different order to prevent
first-mover advantages).

    Player                 Games     Won    Lost    Ties    Diff
    ------------------------------------------------------------
    Max Corner                10       9       1       0     312
    Randy Random              10       5       5       0      22
    Edgar Edge                10       5       5       0     -22
    Max Round                 10       5       4       1     -30
    Max Minimax               10       3       6       1     -27
    Freddy Firstmove          10       2       8       0    -255

### Single Game

Game (`game.py`): play as `StdinPlayer` against the computer.

###  Simulation

Simulation: (`simulation.py`): run a number of simulations of two players
against each other
