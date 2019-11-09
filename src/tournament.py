#!/usr/bin/env python3

from board import Board
from game import Game, Result
from random_player import RandomPlayer
from maxround_player import MaxroundPlayer
from edge_player import EdgePlayer


class TournamentPlayer:

    def __init__(self, clazz, name):
        self._class = clazz
        self._name = name
        self._won = 0
        self._lost = 0
        self._ties = 0
        self._delta = 0

    def spawn(self, field):
        return self._class(self._name, field)

    def __repr__(self):
        return '{} {}'.format(self._name, self._class.__name__)


class Tournament:

    def __init__(self, players):
        self._pairings = self.pair_up(players)

    def pair_up(self, players):
        n_players = len(players)
        if n_players < 2:
            raise ValueError('unable to play tournament with {} players'
                             .format(n_players))

        pairings = []
        for i in range(n_players):
            for j in range(i+1, n_players):
                first = players[i]
                second = players[j]
                pairings.append((first, second))
                pairings.append((second, first))

        return pairings

    def play(self, rounds):
        if rounds < 1:
            raise ValueError('cannot play less than 0 rounds')

        for round in range(rounds):
            for pairing in self._pairings:
                black_player = pairing[0].spawn(Board.FIELD_BLACK)
                white_player = pairing[1].spawn(Board.FIELD_WHITE)

                game = Game(black_player, white_player)
                result, diff = game.play()

                if result == Result.TIE:
                    pairing[0]._ties += 1
                    pairing[1]._ties += 1
                if result == Result.BLACK_WINS:
                    pairing[0]._won += 1
                    pairing[0]._delta += diff
                    pairing[1]._lost += 1
                    pairing[1]._delta -= diff
                if result == Result.WHITE_WINS:
                    pairing[0]._lost += 1
                    pairing[0]._delta -= diff
                    pairing[1]._won += 1
                    pairing[1]._delta += diff

        results = []
        for player in self._pairings:
            played = player[0]._won + player[0]._lost + player[0]._ties
            entry = {'name': player[0]._name, 'won': player[0]._won,
                     'lost': player[0]._lost, 'ties': player[0]._ties,
                     'delta': player[0]._delta, 'played': played}
            if entry not in results:
                results.append(entry)
        return results


def output_table(result):
    result = sorted(result, key=lambda entry: entry['delta'], reverse=True)
    result = sorted(result, key=lambda entry: entry['won'], reverse=True)
    print('{:<20s}{:<8s}{:>8s}{:>8s}{:>8s}{:>8s}'
          .format('Player', 'Games', 'Won', 'Lost', 'Ties', 'Diff'))
    print(60 * '-')
    for player in result:
        print('{:20s}{:8d}{:8d}{:8d}{:8d}{:8d}'
              .format(player['name'], player['played'], player['won'],
                      player['lost'], player['ties'], player['delta']))


if __name__ == '__main__':
    randy = TournamentPlayer(RandomPlayer, 'Randy Random')
    maxi = TournamentPlayer(MaxroundPlayer, 'Max Hardcore')
    edge = TournamentPlayer(EdgePlayer, 'Edgar Edge')
    tournament = Tournament([randy, maxi, edge])
    result = tournament.play(10)
    output_table(result)
