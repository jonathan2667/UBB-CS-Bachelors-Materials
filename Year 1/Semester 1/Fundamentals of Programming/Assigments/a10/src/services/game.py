from src.domain.board import Board, WIDTH, HEIGHT
import numpy as np
import math
import random
class Game:
    def __init__(self):
        self.__board = Board()
        self.__game_over = False
        self.__turn = 0

    @property
    def game_over(self):
        return self.__game_over

    @game_over.setter
    def game_over(self, value):
        self.__game_over = value

    @property
    def turn(self):
        return self.__turn

    @property
    def board(self):
        return self.__board

    def get_board(self):
        return np.flip(self.board.board, 0)

    def change_turn(self):
        self.__turn = (self.turn + 1) % 2

    def drop_piece(self, column):
        next_row = self.get_next_open_row(column)
        if next_row != -1:  # Ensure the row is valid
            self.__board.board[next_row][column] = self.turn + 1
            self.change_turn()
        else:
            print(f"Column {column + 1} is full. Please choose a different column.")

    def is_valid_column(self, column):
        return column >= 0 and column < WIDTH and self.__board.board[HEIGHT - 1][column] == 0

    def get_next_open_row(self, column):
        for row in range(HEIGHT):
            if self.__board.board[row][column] == 0:
                return row
        return -1  # Indicates the column is full

    def is_draw(self):
        return np.count_nonzero(self.__board.board) == WIDTH * HEIGHT

    def winning_move(self, column: int):
        row = self.get_next_open_row(column) - 1
        if row == -1:
            return False

        if row >= 3 and self.__board.board[row][column] == self.__board.board[row - 1][column] == self.__board.board[row - 2][
            column] == self.__board.board[row - 3][column]:
            self.__game_over = True
            return True

        for gap in range(4):
            top_horizontal = row - gap
            top_vertical = column + gap

            if top_vertical < WIDTH and top_vertical - 3 >= 0:
                if self.__board.board[row][top_vertical] == self.__board.board[row][top_vertical - 1] == self.__board.board[row][
                    top_vertical - 2] == self.__board.board[row][top_vertical - 3]:
                    self.__game_over = True
                    return True
                if top_horizontal >= 0 and top_horizontal + 3 < HEIGHT:
                    if self.__board.board[top_horizontal][top_vertical] == self.__board.board[top_horizontal + 1][top_vertical - 1] == \
                            self.__board.board[top_horizontal + 2][top_vertical - 2] == self.__board.board[top_horizontal + 3][top_vertical - 3]:
                        self.__game_over = True
                        return True

            top_vertical = column - gap

            if top_horizontal >= 0 and top_vertical >= 0 and top_horizontal + 3 < HEIGHT and top_vertical + 3 < WIDTH:
                if self.__board.board[top_horizontal][top_vertical] == self.__board.board[top_horizontal + 1][top_vertical + 1] == \
                        self.__board.board[top_horizontal + 2][top_vertical + 2] == self.__board.board[top_horizontal + 3][top_vertical + 3]:
                    self.__game_over = True
                    return True

        return False