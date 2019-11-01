import numpy as np

class Board:

    DIM = 8

    FIELD_EMPTY = 0
    FIELD_P1 = 1
    FIELD_P2 = 2


    def __init__(self):
        self.__fields  = np.zeros([self.DIM, self.DIM], dtype=np.uint8)


    @property
    def fields(self):
        return self.__fields
