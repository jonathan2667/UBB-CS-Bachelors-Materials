from src.board.text_file_board import TextFileBoard
from src.domain.computer import Computer


class Ui:
    @staticmethod
    def menu():
        print("        Welcome to Order & Chaos!")
        print()
        print(" 1 - New Game")
        print(" 2 - Load Game")
        print(" 0 - Exit")

    @staticmethod
    def gameplay(board):
        chaos = Computer(board)
        print(board)
        while not board.draw():
            while True:
                try:
                    print()
                    move = input("Enter coords and symbol (i,j,symbol): ")
                    print()
                    break
                except ValueError as ve:
                    print("Invalid move!", ve)
            valid = False
            i, j, symbol = chaos.place()
            while not valid:
                if move.strip() == "load":
                    board.save()
                    return
                array = move.split(",")
                if len(array) == 3:
                    if array[0].isdigit() and array[1].isdigit():
                        if array[2].strip() == "X" or array[2].strip() == "O":
                            try:
                                board.place(int(array[0]), int(array[1]), array[2])
                                valid = True
                            except ValueError as ve:
                                print(ve)
                        else:
                            print("Symbol must be 'X' or 'O'!")
                    else:
                        print("Coordinates must be integers!")
                else:
                    print("To less or too many input parameters!")
                if not valid:
                    print()
                    move = input("Enter coords and symbol (i,j,symbol): ")
                    print()
            print(board)
            print(f"AI:({i},{j},{symbol}), Human:({move})")
            if board.win():
                print()
                print("Order WINS!")
                print()
                return
        print()
        print("Chaos WINS!")

    def run_game(self):
        self.menu()
        while True:
            while True:
                try:
                    print()
                    option = int(input("Enter your choice: "))
                    print()
                    break
                except ValueError as ve:
                    print("Invalid choice!", ve)
            if option == 1:
                board = TextFileBoard(False)
                self.gameplay(board)
            elif option == 2:
                board = TextFileBoard(True)
                self.gameplay(board)
            elif option == 0:
                print("Game exited successfully!")
                break
            else:
                print("Invalid choice!")
