import random

import texttable as texttable


class Board:
    def __init__(self):
        self.__data = [[" " for _ in range(8)] for _ in range(8)]
        self.__visible = [[False for _ in range(8)] for _ in range(8)]

    def __str__(self):
        board = texttable.Texttable()
        board.header(list(range(0, 9)))
        for i in range(8):
            row = [chr(ord('A') + i)]
            for j in range(8):
                if self.__visible[i][j]:
                    row.append(self.__data[i][j])
                else:
                    row.append(" ")
            board.add_row(row)
        return board.draw()

    def get_endeavour_position(self):
        for i in range(8):
            for j in range(8):
                if self.__data[i][j] == "🚀":
                    self.__visible[i][j] = True
                    return i, j
        return -1, -1

    def placing_stars(self):
        counter = 0
        locked = [[True for _ in range(8)] for _ in range(8)]
        while counter != 10:
            i = random.randint(0, 7)
            j = random.randint(0, 7)
            if self.__data[i][j] == " " and locked[i][j]:
                self.__data[i][j] = "⭐"
                self.__visible[i][j] = True
                for x in range(8):
                    for y in range(8):
                        if -1 < i - 1 < 8 and -1 < j < 8:
                            # up
                            locked[i - 1][j] = False
                        if -1 < i - 1 < 8 and -1 < j - 1 < 8:
                            # up - left
                            locked[i - 1][j - 1] = False
                        if -1 < i - 1 < 8 and -1 < j + 1 < 8:
                            # up -right
                            locked[i - 1][j + 1] = False
                        if -1 < i < 8 and -1 < j + 1 < 8:
                            # right
                            locked[i][j + 1] = False
                        if -1 < i + 1 < 8 and -1 < j + 1 < 8:
                            # down - right
                            locked[i + 1][j + 1] = False
                        if -1 < i + 1 < 8 and -1 < j < 8:
                            # down
                            locked[i + 1][j] = False
                        if -1 < i + 1 < 8 and -1 < j - 1 < 8:
                            # down - left
                            locked[i + 1][j - 1] = False
                        if -1 < i < 8 and -1 < j - 1 < 8:
                            # left
                            locked[i][j - 1] = False
                counter += 1

    def placing_endeavour(self):
        placed = False
        while not placed:
            i = random.randint(0, 7)
            j = random.randint(0, 7)
            if self.__data[i][j] == " ":
                self.__data[i][j] = "🚀"
                self.__visible[i][j] = True
                placed = True

    def placing_enemies(self):
        number = random.randint(3, 5)
        counter = 0
        while counter != number:
            i = random.randint(0, 7)
            j = random.randint(0, 7)
            if self.__data[i][j] == " ":
                self.__data[i][j] = "👽"
                self.__visible[i][j] = False
                counter += 1
        return number

    def replacing_enemies(self):
        number = self.count_enemies()
        for x in range(8):
            for y in range(8):
                if self.__data[x][y] == "👽":
                    self.__data[x][y] = ""
        counter = 0
        while counter != number:
            i = random.randint(0, 7)
            j = random.randint(0, 7)
            if self.__data[i][j] == " ":
                self.__data[i][j] = "👽"
                self.__visible[i][j] = False
                counter += 1

    def player_visibility(self):
        for x in range(8):
            for y in range(8):
                if self.__data[x][y] == "👽":
                    self.__visible[x][y] = False
        i, j = self.get_endeavour_position()
        for x in range(8):
            for y in range(8):
                if -1 < i - 1 < 8 and -1 < j < 8:
                    # up
                    self.__visible[i - 1][j] = True
                if -1 < i - 1 < 8 and -1 < j - 1 < 8:
                    # up - left
                    self.__visible[i - 1][j - 1] = True
                if -1 < i - 1 < 8 and -1 < j + 1 < 8:
                    # up -right
                    self.__visible[i - 1][j + 1] = True
                if -1 < i < 8 and -1 < j + 1 < 8:
                    # right
                    self.__visible[i][j + 1] = True
                if -1 < i + 1 < 8 and -1 < j + 1 < 8:
                    # down - right
                    self.__visible[i + 1][j + 1] = True
                if -1 < i + 1 < 8 and -1 < j < 8:
                    # down
                    self.__visible[i + 1][j] = True
                if -1 < i + 1 < 8 and -1 < j - 1 < 8:
                    # down - left
                    self.__visible[i + 1][j - 1] = True
                if -1 < i < 8 and -1 < j - 1 < 8:
                    # left
                    self.__visible[i][j - 1] = True

    def warp(self, i, j):
        x, y = self.get_endeavour_position()
        if self.__data[i - 1][j - 1] == " ":
            if x == i - 1 or y == j - 1 or abs(x - (i - 1)) == abs(y - (j - 1)):
                self.__data[i - 1][j - 1] = "🚀"
                self.__visible[i - 1][j - 1] = True
                self.__data[x][y] = " "
                self.player_visibility()
                return True
            else:
                raise ValueError("The ship cannot warp this way!")
        elif self.__data[i - 1][j - 1] == "👽":
            return False
        else:
            raise ValueError("Occupied!")

    def cheat(self):
        for x in range(8):
            for y in range(8):
                self.__visible[x][y] = True

    def count_enemies(self):
        counter = 0
        for x in range(8):
            for y in range(8):
                if self.__data[x][y] == "👽":
                    counter += 1
        return counter

    def win(self):
        for x in range(8):
            for y in range(8):
                if self.__data[x][y] == "👽":
                    return False
        return True

    def fire(self, i, j):
        self.player_visibility()
        for x in range(8):
            for y in range(8):
                if self.__visible[i - 1][j - 1] is True:
                    if self.__data[i - 1][j - 1] != "⭐":
                        if self.__data[i - 1][j - 1] == "👽":
                            self.__data[i - 1][j - 1] = " "
                            return True
                        else:
                            return False
                    else:
                        raise ValueError("You cannot hit stars!")
                else:
                    raise ValueError("You can hit only in neighbouring squares!")
