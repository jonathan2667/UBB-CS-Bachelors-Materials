from src.board.board import Board


class TextFileBoard(Board):
    def __init__(self, load):
        super().__init__()
        self.__file_name = "saved_game"
        if load:
            self.__load()

    def __load(self):
        with open(self.__file_name, "r") as f:
            i = 1
            for line in f:
                if '|' in line:
                    array = line.split("|")
                    for j in range(7):
                        if array[j].strip() == "O" or array[j].strip() == "X":
                            super().place(i, j, array[j].strip())
                        else:
                            self.set_empty(i, j)
                    i += 1

    def save(self):
        with open(self.__file_name, "w") as f:
            f.write(self.__str__())
