import numpy as np

class Board:

    DIM = 8

    FIELD_EMPTY = 0
    FIELD_BLACK = 1
    FIELD_WHITE = 2


    def __init__(self):
        self.__fields = np.zeros([self.DIM, self.DIM], dtype=np.uint8)

        whites = [[self.DIM/2-1, self.DIM/2-1], [self.DIM/2, self.DIM/2]]
        blacks = [[self.DIM/2, self.DIM/2-1], [self.DIM/2-1, self.DIM/2]]

        for [r, c] in whites:
            self.__fields[(int(r), int(c))] = self.FIELD_WHITE
        for [r, c] in blacks:
            self.__fields[(int(r), int(c))] = self.FIELD_BLACK


    @property
    def fields(self):
        return self.__fields
