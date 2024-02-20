from src.services.game import Game
from src.services.ai import AI
import math
class UI:
    def __init__(self):
        self.__game = Game()
        self.__ai = AI(6)
        self.__depth = 6
        self.__tokens = ["\U000026aa", "\U0001f534", "\U0001f7e1"]

    def print_board(self):
        board = self.__game.get_board()
        for row in board:
            for column in row:
                print(self.__tokens[column], end=" ")
            print()


    def run(self):
        print("Welcome to Connect Four!")
        print("1. Play against a friend")
        print("2. Play against the computer")
        print("3. Computer against computer")
        print("4. Exit")

        try:
            game_option = int(input())

            if game_option == 1:
                print("You chose to play against a friend!")
                self.play_against_friend()
            elif game_option == 2:
                print("You chose to play against the computer!")
                self.play_against_computer()
            elif game_option == 3:
                print("You chose to watch the computer play against itself!")
                self.computer_against_computer()
            else:
                print("Invalid game option!")
                self.run()

        except ValueError:
            print("Invalid game_option!")
            self.run()

    def player_turn(self):
        column = int(input("Player " + str(self.__game.turn + 1) +
                        "\nMake your selection(1-7): ")) - 1
        if self.__game.is_valid_column(column):
            self.__game.drop_piece(column)
            self.print_board()
            if self.__game.winning_move(column):
                print("Player " + str(self.__game.turn + 1) + " wins!")
                #self.__game.game_over = True
            elif self.__game.is_draw():
                print("It's a draw!")
                #self.__game.game_over = True
        else:
            print("Invalid column!")
            self.player_turn()

    def computer_turn(self):
        print("AI's turn!")
        ai_col = self.__ai.minimax(
            self.__game.board, self.__depth, -math.inf, math.inf, True)[0]
        self.__game.drop_piece(ai_col)
        self.print_board()
        if self.__game.winning_move(ai_col):
            print("AI won!")
        if self.__game.is_draw():
            print("Draw!")

    def play_against_friend(self):
        while not self.__game.game_over:
            self.player_turn()
            if not self.__game.game_over:
                self.player_turn()

    def play_against_computer(self):
        while not self.__game.game_over:
            self.player_turn()
            if not self.__game.game_over:
                self.computer_turn()

    def computer_against_computer(self):
        while not self.__game.game_over:
            self.computer_turn()
            if not self.__game.game_over:
                self.computer_turn()
