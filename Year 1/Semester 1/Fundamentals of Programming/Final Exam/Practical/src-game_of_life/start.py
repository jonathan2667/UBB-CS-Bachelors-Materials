from src.board.text_file_board import TextFileBoard
from src.ui.ui import Ui

if __name__ == "__main__":
    board = TextFileBoard()
    ui = Ui(board)
    ui.run_app()
