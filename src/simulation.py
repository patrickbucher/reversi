#!/usr/bin/env python3

import sys

from board import Board
from game import Game, Result
from random_player import RandomPlayer
from maxround_player import MaxroundPlayer

if __name__ == '__main__':

    n_games = 1000
    if len(sys.argv) > 1:
        n_games = int(sys.argv[1])
        if n_games < 0:
            raise ValueError('cannot run negative number of games')

    player_black = MaxroundPlayer('Max Round', Board.FIELD_BLACK)
    player_white = RandomPlayer('Barry White', Board.FIELD_WHITE)

    black_wins, white_wins, ties = 0, 0, 0
    black_diff, white_diff = 0, 0

    for i in range(n_games):
        game = Game(player_black, player_white)
        result, diff = game.play()
        if result == Result.BLACK_WINS:
            black_wins += 1
            black_diff += diff
        elif result == Result.WHITE_WINS:
            white_wins += 1
            white_diff += diff
        else:
            ties += 1

    black_delta = black_diff - white_diff
    white_delta = white_diff - black_diff
    print('Black Wins: {:4d} (Δ {:4d})'.format(black_wins, black_delta))
    print('White Wins: {:4d} (Δ {:4d})'.format(white_wins, white_delta))
    print('Ties:       {:4d}'.format(ties))
