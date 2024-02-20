import copy
import math
from src.domain.board import HEIGHT, WIDTH, Board

class AI:
    def __init__(self,depth):
        self.__depth = depth
        self.__columns_array = [3, 4, 2, 1, 5, 0, 6]
        self.__AI = 2
        self.__HUMAN = 1
        self.__MAX_VALUE = 100000

    def set_depth(self,depth):
        self.__depth = depth

    def winning_move(self, board: Board, player):
        # Look after horizontal locations for win
        for row in range(HEIGHT):
            for column in range(WIDTH - 3):
                if board.board[row][column] == board.board[row][column + 1] == board.board[row][column + 2] == board.board[row][
                    column + 3] == player:
                    return True

        for row in range(HEIGHT - 3):
            for column in range(WIDTH):
                if board.board[row][column] == board.board[row + 1][column] == board.board[row + 2][column] == \
                        board.board[row + 3][column] == player:
                    return True
            for column in range(WIDTH - 1, 2, -1):
                if board.board[row][column] == board.board[row + 1][column - 1] == board.board[row + 2][column - 2] == \
                        board.board[row + 3][column - 3] == player:
                    return True
            for column in range(WIDTH - 3):
                if board.board[row][column] == board.board[row + 1][column + 1] == board.board[row + 2][column + 2] == \
                        board.board[row + 3][column + 3] == player:
                    return True
        return False

    def get_tokens_score(self, tokens):
        score = 0

        counter = tokens.count(self.__AI)
        opponent_cnt = tokens.count(self.__HUMAN)

        if counter == 4:
            score += 1000
        elif opponent_cnt == 0:
            if counter == 3:
                score += 100
            elif counter == 2:
                score += 1
        if opponent_cnt == 3 and counter == 0:
            score -= 500

        return score

    def get_board_score(self, board: Board):
        score = 0

        for col in self.__columns_array:
            col_array = [i for i in list(board.board[:, col])]
            for row in range(HEIGHT - 3):
                tokens = col_array[row:row + 4]
                score += self.get_tokens_score(tokens)

        for row in range(HEIGHT):
            row_array = [i for i in list(board.board[row, :])]
            for col in range(WIDTH - 3):
                tokens = row_array[col:col + 4]
                score += self.get_tokens_score(tokens)

        for row in range(HEIGHT - 3):
            for col in range(WIDTH - 3):
                tokens = [board.board[row + i][col + i] for i in range(4)]
                score += self.get_tokens_score(tokens)

        for row in range(HEIGHT - 3):
            for col in range(WIDTH - 3):
                tokens = [board.board[row + 3 - i][col + i] for i in range(4)]
                score += self.get_tokens_score(tokens)

        return score

    def get_next_open_row(self, board, col):
        for row in range(HEIGHT):
            if board.board[row][col] == 0:
                return row
        return 0

    def is_valid_location(self, board: Board, col: int):
        return board.board[HEIGHT - 1][col] == 0
    def get_valid_columns(self, board: Board):
        return [int(col) for col in self.__columns_array if self.is_valid_location(board, col)]

    def drop_piece(self, board: Board, col: int, player: int):
        board.board[self.get_next_open_row(board, col)][col] = player

    def terminal(self, board: Board):
        return self.winning_move(board, self.__AI) or self.winning_move(board, self.__HUMAN) or len(
            self.get_valid_columns(board)) == 0

    def minimax(self, board: Board, depth, alpha, beta, maximizingPlayer):
        valid_columns = self.get_valid_columns(board)

        terminal = self.terminal(board)

        if depth == 0 or terminal:
            if terminal:
                if self.winning_move(board, self.__AI):
                    return (None, self.__MAX_VALUE)

                elif self.winning_move(board, self.__HUMAN):
                    return (None, -self.__MAX_VALUE)

                else:
                    return (None, 0)
            else:
                return (None, self.get_board_score(board))

        if maximizingPlayer:
            value = -math.inf
            column = valid_columns[0]

            if depth == self.__depth:
                for col in valid_columns:
                    new_board = copy.deepcopy(board)
                    self.drop_piece(new_board, col, self.__AI)
                    if self.winning_move(new_board, self.__AI):
                        return col, None

            for col in valid_columns:
                new_board = copy.deepcopy(board)
                self.drop_piece(new_board, col, self.__AI)
                new_score = self.minimax(new_board, depth - 1, alpha, beta, False)[1]

                if new_score > value:
                    value = new_score
                    column = col

                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return column, value

        else:
            value = math.inf
            column = valid_columns[0]
            for col in valid_columns:
                new_board = copy.deepcopy(board)
                self.drop_piece(new_board, col, self.__HUMAN)
                new_score = self.minimax(new_board, depth - 1, alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return column, value