from unittest import TestCase

from src.board.board import Board


class TestBoard(TestCase):
    def setUp(self) -> None:
        self.board = Board()

    def test_win_on_horizontal_line(self):
        for i in range(1, 6):
            self.board.place(1, i, "X")
        self.assertTrue(self.board.win())

    def test_win_on_vertical_line(self):
        for i in range(1, 6):
            self.board.place(i, 1, "X")
        self.assertTrue(self.board.win())

    def test_win_on_diagonal_line_right_to_left(self):
        for i in range(1, 6):
            self.board.place(i, i, "X")
        self.assertTrue(self.board.win())

    def test_win_on_diagonal_line_left_to_right(self):
        for i in range(1, 6):
            self.board.place(i, 6 - i, "X")
        self.assertTrue(self.board.win())

    def tearDown(self) -> None:
        pass