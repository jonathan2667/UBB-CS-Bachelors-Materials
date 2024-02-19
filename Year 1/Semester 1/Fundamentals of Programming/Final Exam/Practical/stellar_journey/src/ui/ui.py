class Ui:
    def __init__(self, board):
        self.__board = board

    def warp(self, i, j):
        try:
            game_over = self.__board.warp(i, j)
        except ValueError as ve:
            print(ve)
            return
        return game_over

    def cheat(self):
        self.__board.cheat()

    def fire(self, i, j):
        try:
            hit = self.__board.fire(i, j)
        except ValueError as ve:
            print(ve)
            return
        return hit

    def setup(self):
        self.__board.placing_stars()
        self.__board.placing_endeavour()
        self.__board.placing_enemies()
        self.__board.player_visibility()
        print(self.__board)

    def gameplay(self):
        self.setup()
        while True:
            while True:
                try:
                    option = input("> ")
                    break
                except ValueError as ve:
                    print("Invalid option", ve)
            array = option.split(" ")
            if len(array) == 2:
                if array[0].strip() == "warp":
                    position = array[1]
                    if position[1].isdigit():
                        game_over = self.warp(int(ord(position[0]) - ord('A') + 1), int(position[1]))
                        if game_over is False:
                            self.cheat()
                            print(self.__board)
                            print("You LOST!")
                            break
                        print(self.__board)
                if array[0].strip() == "fire":
                    position = array[1]
                    if position[1].isdigit():
                        hit = self.fire(int(ord(position[0]) - ord('A') + 1), int(position[1]))
                        if hit is True:
                            print("You hit an enemy!")
                            self.__board.replacing_enemies()
                            self.__board.player_visibility()
                        else:
                            print("You missed!")
                        print(self.__board)
            elif len(array) == 1:
                if array[0].strip() == "cheat":
                    self.cheat()
                    print(self.__board)
                # elif array[0].strip() == "exit":
                #     print("Game was exited successfully!")
                #     break
                else:
                    print("Invalid option!")
            if self.__board.win():
                print("You WON!")
                break
