from src.board.board import Board
from src.ui.ui import Ui

if __name__ == "__main__":
    board = Board()
    ui = Ui(board)
    ui.gameplay()

