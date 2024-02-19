class Ui:
    def __init__(self, board):
        self.__board = board

    def run_app(self):
        print(self.__board)
        while True:
            while True:
                try:
                    print()
                    option = input("> ")
                    print()
                    break
                except ValueError as ve:
                    print("Invalid input!", ve)
            array = option.split(" ")
            if len(array) == 4:
                if array[0].strip() == "place":
                    if array[2].isdigit() and array[3].isdigit():
                        if array[1].strip() == "block":
                            try:
                                self.__board.place_block(int(array[2]), int(array[3]))
                                print(self.__board)
                            except ValueError as ve:
                                print(ve)
                        elif array[1].strip() == "tub":
                            try:
                                self.__board.place_tub(int(array[2]), int(array[3]))
                                print(self.__board)
                            except ValueError as ve:
                                print(ve)
                        elif array[1].strip() == "blinker":
                            try:
                                self.__board.place_blinker(int(array[2]), int(array[3]))
                                print(self.__board)
                            except ValueError as ve:
                                print(ve)
                        elif array[1].strip() == "beacon":
                            try:
                                self.__board.place_beacon(int(array[2]), int(array[3]))
                                print(self.__board)
                            except ValueError as ve:
                                print(ve)
                        elif array[1].strip() == "spaceship":
                            try:
                                self.__board.place_spaceship(int(array[2]), int(array[3]))
                                print(self.__board)
                            except ValueError as ve:
                                print(ve)
                        else:
                            print("Nonexistent shape!")
                    else:
                        print("Coordinates must be integers between 1 to 8!")
                else:
                    print("Invalid option!")
            elif len(array) == 2:
                if array[0].strip() == "tick":
                    if array[1].isnumeric():
                        for i in range(int(array[1])):
                            self.__board.advancing()
                        print(self.__board)
                    else:
                        print("Parameter for 'tick' must be an integer or just the command!")
                else:
                    print("Invalid option!")
            elif len(array) == 1:
                if array[0].strip() == "tick":
                    self.__board.advancing()
                    print(self.__board)
                elif array[0].strip() == "save":
                    # self.__board.set_file_name(array[1])
                    self.__board.save()
                    self.__board.load()
                elif array[0].strip() == "load":
                    # self.__board.set_file_name(array[1])
                    self.__board.load()
                    print(self.__board)
                else:
                    print("Invalid option!")
            else:
                print("Invalid option!")
