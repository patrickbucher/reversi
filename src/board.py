import numpy as np


class Board:

    DIM = 8
    FIELD_EMPTY = 0
    FIELD_BLACK = 1
    FIELD_WHITE = 2

    NORTH = (-1, 0)
    NORTH_EAST = (-1, 1)
    EAST = (0, 1)
    SOUTH_EAST = (1, 1)
    SOUTH = (1, 0)
    SOUTH_WEST = (1, -1)
    WEST = (0, -1)
    NORTH_WEST = (-1, -1)

    DIRECTIONS = [NORTH, NORTH_EAST, EAST, SOUTH_EAST,
                  SOUTH, SOUTH_WEST, WEST, NORTH_WEST]

    def __init__(self, fields):
        if fields.shape != (self.DIM, self.DIM):
            raise ValueError('unsupported dimensions', fields.shape)

        self._fields = fields

    @classmethod
    def start_position(cls):
        fields = np.zeros([cls.DIM, cls.DIM], dtype=np.uint8)

        whites = [[cls.DIM/2-1, cls.DIM/2-1], [cls.DIM/2, cls.DIM/2]]
        blacks = [[cls.DIM/2, cls.DIM/2-1], [cls.DIM/2-1, cls.DIM/2]]

        for [r, c] in whites:
            fields[(int(r), int(c))] = cls.FIELD_WHITE
        for [r, c] in blacks:
            fields[(int(r), int(c))] = cls.FIELD_BLACK

        return Board(fields)

    @classmethod
    def from_fields(cls, fields):
        return Board(fields)

    @property
    def fields(self):
        return self._fields

    def valid_moves(self, color):
        result = []
        empty_fields = self.indices_of(self.FIELD_EMPTY)
        opponent = self.other(color)
        neighbourships = self.adjacent_of(empty_fields, opponent)
        valid = range(0, self.DIM)
        for (orig, delta, opponent_field) in neighbourships:
            p = opponent_field
            while p[0] + delta[0] in valid and p[1] + delta[1] in valid:
                r = p[0] + delta[0]
                c = p[1] + delta[1]
                if self._fields[r][c] == color:
                    result.append(orig)
                    break
                if self._fields[r][c] == opponent:
                    break
                p = (r, c)
        return result

    def adjacent_of(self, fields, color):
        adjacents = []
        for (row, col) in fields:
            for (delta_row, delta_col) in self.DIRECTIONS:
                r = row + delta_row
                c = col + delta_col
                valid = range(0, self.DIM)
                if r not in valid or c not in valid:
                    continue
                if self._fields[r][c] == color:
                    orig = (row, col)
                    dim = (delta_row, delta_col)
                    adjacent = (r, c)
                    adjacents.append((orig, dim, adjacent))
        return adjacents

    def indices_of(self, color):
        (rows, cols) = np.where(self._fields == color)
        return self.list_of_tuples(rows, cols)

    def list_of_tuples(self, rows, cols):
        if rows.size != cols.size:
            raise ValueError('arrays rows and cols of different size')
        result = []
        for i in range(0, rows.size):
            result.append((rows[i], cols[i]))
        return result

    def other(self, color):
        if color == self.FIELD_BLACK:
            return self.FIELD_WHITE
        elif color == self.FIELD_WHITE:
            return self.FIELD_BLACK
        else:
            raise ValueError('unsupported color {:d}'.format(color))
