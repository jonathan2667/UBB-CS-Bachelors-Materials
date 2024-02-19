from src.board.board import Board
from src.computer.computer import Computer


class Ui:
    @staticmethod
    def gameplay():
        player_board = Board(True)
        print("Player's Board")
        print(player_board)
        computer_board = Board(False)
        computer = Computer(computer_board)
        computer_board = computer.placement()
        print("Computer's Board")
        print(computer_board)
        all_ships = []
        while not player_board.win() or not computer_board.win():
            option = ""
            while option.split() != "start":
                try:
                    print()
                    option = input("> ")
                    print()
                    break
                except ValueError as ve:
                    print("Invalid command!", ve)
            array = option.split(" ")
            if len(array) == 2:
                if array[0].strip() == "ship":
                    if len(array[1]) == 6:
                        positions = array[1]
                        if positions[0].isupper() and positions[1].isdigit() and positions[2].isupper() and positions[
                            3].isdigit() and positions[4].isupper() and positions[5].isdigit():
                            try:
                                positions = player_board.place(int(ord(positions[0]) - ord('A')),
                                                               int(positions[1]),
                                                               int(ord(positions[2]) - ord('A')),
                                                               int(positions[3]),
                                                               int(ord(positions[4]) - ord('A')),
                                                               int(positions[5]))
                                all_ships.append(positions)
                                print("Ship was added")
                                print(player_board)
                            except ValueError as ve:
                                print(ve)
                            if len(all_ships) == 2:
                                remove = all_ships[0]
                                player_board.remove_ship(remove[0], remove[1], remove[2], remove[3], remove[4],
                                                         remove[5])
                                del all_ships[0]
