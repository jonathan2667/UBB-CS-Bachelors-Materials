import copy
import random


class Computer:
    def __init__(self, board):
        self.__board = board

    def simulate(self, i, j, symbol):
        temporary_board = copy.deepcopy(self.__board)
        temporary_board.place(i, j, symbol)
        return temporary_board

    def place(self):
        for i in range(1, 7):
            for j in range(1, 7):
                if self.__board.valid(i, j):
                    temp = self.simulate(i, j, "X")
                    if temp.win():
                        self.__board.place(i, j, "X")
                        return i, j, "X"
        for i in range(6):
            for j in range(6):
                if self.__board.valid(i, j):
                    temp = self.simulate(i, j, "O")
                    if temp.win():
                        self.__board.place(i, j, "O")
                        return i, j, "O"
        xs, os = self.__board.count_symbols()
        if xs < os:
            symbol = "X"
        else:
            symbol = "O"
        placed = False
        while not placed:
            i = random.randint(1, 6)
            j = random.randint(1, 6)
            try:
                self.__board.place(i, j, symbol)
                placed = True
                return i, j, symbol
            except ValueError:
                continue
