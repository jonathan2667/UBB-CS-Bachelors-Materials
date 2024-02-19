import random


class Computer:
    def __init__(self, board):
        self.__board = board

    def placement(self):
        placed = False
        i = 0
        while not placed:
            x1 = random.randint(0, 5)
            x2 = random.randint(0, 5)
            x3 = random.randint(0, 5)
            y1 = random.randint(0, 5)
            y2 = random.randint(0, 5)
            y3 = random.randint(0, 5)
            try:
                self.__board.place(x1, y1, x2, y2, x3, y3)
                i += 1
            except ValueError:
                continue
            if i == 2:
                placed = True
        return self.__board
