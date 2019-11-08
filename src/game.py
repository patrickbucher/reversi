#!/usr/bin/env python3

import logging
from enum import Enum

from board import Board
from random_player import RandomPlayer
from stdin_player import StdinPlayer


class Result(Enum):
    TIE = 0
    BLACK_WINS = 1
    WHITE_WINS = 2


class Game:

    def __init__(self, player_black, player_white):
        self._player_black = player_black
        self._player_white = player_white

    def log_level(self, level):
        logging.basicConfig(level=level)

    def play(self):
        board = Board.start_position()
        player = self._player_white
        stuck_counter = 0
        done = False
        while not done:

            logging.debug('field \n{}'.format(board.fields))

            if player == self._player_black:
                player = self._player_white
            else:
                player = self._player_black

            move = player.play(board)
            if move is None:
                logging.debug('player {:s} must pass'.format(player.name))
                stuck_counter += 1
            elif move in board.valid_moves(player.field):
                board = board.play(move, player.field)
                logging.debug('player {:s} move ({:d}, {:d})'
                              .format(player.name, move[0], move[1]))
                stuck_counter = 0
            else:
                logging.warning('player {:s} illegal move ({:d}, {:d})'
                                .format(player.name, move[0], move[1]))

            if stuck_counter == 2:
                logging.warning('game is stuck')
                break

            done, black, white = board.outcome()
            logging.debug('{:s}: {:d}, {:s}: {:d}, finished: {}'.
                          format(self._player_black.name, black,
                                 self._player_white.name, white,
                                 done))

        logging.debug('field \n{}'.format(board.fields))
        if black > white:
            return (Result.BLACK_WINS, black - white)
        elif white > black:
            return (Result.WHITE_WINS, white - black)
        else:
            return (Result.TIE, 0)


if __name__ == '__main__':
    player_black = StdinPlayer('blacky', Board.FIELD_BLACK)
    player_white = RandomPlayer('whitey', Board.FIELD_WHITE)
    game = Game(player_black, player_white)
    game.log_level(logging.DEBUG)
    result, diff = game.play()
    print(result, diff)
