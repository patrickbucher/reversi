import numpy as np


class Board:

    DIM = 8
    FIELD_EMPTY = 0
    FIELD_BLACK = 1
    FIELD_WHITE = 2

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
