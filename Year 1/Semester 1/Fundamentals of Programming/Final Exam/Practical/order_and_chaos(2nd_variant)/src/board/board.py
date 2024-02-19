import texttable


class Board:
    def __init__(self):
        self.__data = [[" " for _ in range(6)] for _ in range(6)]

    def __str__(self):
        board = texttable.Texttable()
        for i in range(6):
            row = []
            for j in range(6):
                if self.__data[i][j] != " ":
                    row.append(self.__data[i][j])
                else:
                    row.append(" ")
            board.add_row(row)
        return board.draw()

    def place(self, i, j, symbol):
        if i < 0 or i > 7 or j < 0 or j > 7:
            raise ValueError("The coordinates must be between 1 and 6!")
        if self.__data[i - 1][j - 1] != " ":
            raise ValueError("This space is occupied!")
        self.__data[i - 1][j - 1] = symbol

    def draw(self):
        for i in range(6):
            for j in range(6):
                if self.__data[i][j] == " ":
                    return False
        return True

    def win(self):
        # Checks lines
        for i in range(6):
            for j in range(2):
                if self.__data[i][j] != " ":
                    if self.__data[i][j] == self.__data[i][j + 1]:
                        if self.__data[i][j] == self.__data[i][j + 2]:
                            if self.__data[i][j] == self.__data[i][j + 3]:
                                if self.__data[i][j] == self.__data[i][j + 4]:
                                    return True
        # Checks columns
        for i in range(2):
            for j in range(6):
                if self.__data[i][j] != " ":
                    if self.__data[i][j] == self.__data[i + 1][j]:
                        if self.__data[i][j] == self.__data[i + 2][j]:
                            if self.__data[i][j] == self.__data[i + 3][j]:
                                if self.__data[i][j] == self.__data[i + 4][j]:
                                    return True
        # Checks diagonal (from left to right)
        for i in range(2):
            for j in range(2):
                if self.__data[i][j] != " ":
                    if self.__data[i][j] == self.__data[i + 1][j + 1]:
                        if self.__data[i][j] == self.__data[i + 2][j + 2]:
                            if self.__data[i][j] == self.__data[i + 3][j + 3]:
                                if self.__data[i][j] == self.__data[i + 4][j + 4]:
                                    return True
        # Checks diagonal (from right to left)
        for i in range(2):
            for j in range(5, 3, -1):
                if self.__data[i][j] != " ":
                    if self.__data[i][j] == self.__data[i + 1][j - 1]:
                        if self.__data[i][j] == self.__data[i + 2][j - 2]:
                            if self.__data[i][j] == self.__data[i + 3][j - 3]:
                                if self.__data[i][j] == self.__data[i + 4][j - 4]:
                                    return True
        return False

    def valid(self, i, j):
        if self.__data[i - 1][j - 1] == " ":
            return True
        return False

    def set_empty(self, i, j):
        self.__data[i - 1][j - 1] = " "

    def get_data(self):
        return self.__data

    def count_symbols(self):
        cx = 0
        co = 0
        for i in range(6):
            for j in range(6):
                if self.__data[i][j] == "X":
                    cx += 1
                elif self.__data[i][j] == "O":
                    co += 1
        return cx, co
