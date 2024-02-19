class Board:
    def __init__(self, visible):
        self.__data = [["." for _ in range(6)] for _ in range(6)]
        self.__visibility = [[visible for _ in range(6)] for _ in range(6)]

    def __str__(self):
        board = "  A B C D E F \n"
        for i in range(6):
            board += str(i)
            board += " "
            for j in range(6):
                if self.__visibility[i][j]:
                    board += self.__data[i][j]
                else:
                    board += "."
                board += " "
            board += "\n"
        return board

    def place(self, y1, x1, y2, x2, y3, x3):
        if self.check_correct_placement(y1, x1, y2, x2, y3, x3):
            if self.__data[x1][y1] == ".":
                if self.__data[x2][y2] == ".":
                    if self.__data[x3][y3] == ".":
                        self.__data[x1][y1] = "+"
                        self.__data[x2][y2] = "+"
                        self.__data[x3][y3] = "+"
                        return [y1, x1, y2, x2, y3, x3]
                    else:
                        raise ValueError("Spot already occupied!")
                else:
                    raise ValueError("Spot already occupied!")
            else:
                raise ValueError("Spot already occupied!")
        else:
            raise ValueError("Incorrect placement!")

    @staticmethod
    def check_correct_placement(y1, x1, y2, x2, y3, x3):
        temporary_data = [["." for _ in range(6)] for _ in range(6)]
        temporary_data[x1][y1] = "+"
        temporary_data[x2][y2] = "+"
        temporary_data[x3][y3] = "+"

        for i in range(6):
            for j in range(4):
                if temporary_data[i][j] != ".":
                    if temporary_data[i][j] == temporary_data[i][j + 1]:
                        if temporary_data[i][j] == temporary_data[i][j + 2]:
                            return True
        for i in range(4):
            for j in range(6):
                if temporary_data[i][j] != ".":
                    if temporary_data[i][j] == temporary_data[i + 1][j]:
                        if temporary_data[i][j] == temporary_data[i + 2][j]:
                            return True
        return False

    def remove_ship(self, y1, x1, y2, x2, y3, x3):
        self.__data[x1][y1] = "."
        self.__data[x2][y2] = "."
        self.__data[x3][y3] = "."

    def win(self):
        for i in range(6):
            for j in range(6):
                if self.__data[i][j] == "+":
                    return False
        return True
